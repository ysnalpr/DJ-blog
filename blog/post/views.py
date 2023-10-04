from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.annotate(total_posts=Count("posts"))
    post_list = Post.published.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post_list = post_list.filter(category=category)
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
    return render(
        request,
        "post/list.html",
        {"posts": posts, "categories": categories, "category": category},
    )


def post_detail(request, year, month, day, post):
    categories = Category.objects.annotate(total_posts=Count("posts"))
    absolute_url = request.build_absolute_uri()
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(
        request,
        "post/detail.html",
        {"post": post, "categories": categories, "absolute_url": absolute_url},
    )

# TODO: Display categories
# TODO: Display tags
# TODO: Render the template based on the category slug
# TODO: Use Postgres database
