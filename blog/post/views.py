from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page number is not an integer return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page number is out of range return the last page.
        posts = paginator.page(paginator.num_pages)
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "post/detail.html", {"post": post})

# TODO: Display categories
# TODO: Display tags
# TODO: Render the template based on the category slug
# TODO: Use Postgres database
