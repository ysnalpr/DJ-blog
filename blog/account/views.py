from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from post.models import Post


class Dashboard(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, "account/dashboard.html")


class AuthorMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class AuthorEditMixin:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorPostMixin(
    AuthorMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin
):
    model = Post
    fields = ["title", "slug", "image", "body", "category", "tags", "status"]
    success_url = reverse_lazy("account:author_post_list")


class AuthorPostEditMixin(AuthorPostMixin, AuthorEditMixin):
    template_name = "account/post/form.html"


class AuthorPostListView(AuthorPostMixin, ListView):
    template_name = "account/post/list.html"
    permission_required = "posts.view_post"


class PostCreateView(AuthorPostEditMixin, CreateView):
    permission_required = "posts.add_post"
    success_message = "Post successfully created."


class PostUpdateView(AuthorPostEditMixin, UpdateView):
    permission_required = "posts.change_post"
    success_message = "Post successfully edited."


class PostDeleteView(AuthorPostMixin, DeleteView):
    template_name = "account/post/delete.html"
    permission_required = "posts.delete_post"
    success_message = "Post successfully deleted."


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        author_group = Group.objects.get(name="Authors")
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            author_group.user_set.add(new_user)
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})


# Edit the User Account and Profile
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("account:dashboard")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
