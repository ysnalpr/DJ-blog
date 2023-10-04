from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    template_name = "post/list.html"
    context_object_name = "posts"
    paginate_by = 3
    category = None

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            return Post.published.filter(category=self.category)
        return Post.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(total_posts=Count("posts"))
        context["category"] = self.category
        return context


class PostDetailView(DetailView):
    template_name = "post/detail.html"

    def get_object(self):
        slug = self.kwargs.get("slug")
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        day = self.kwargs.get("day")
        post = get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            slug=slug,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(total_posts=Count("posts"))
        context["absolute_url"] = self.request.build_absolute_uri()
        return context
