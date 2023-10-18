from django import template
from ..models import Category, Post

register = template.Library()


@register.inclusion_tag("post/show_categories.html")
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag("post/latest_posts.html")
def show_latest_post(count=5):
    latest_post = Post.published.order_by("-publish")[:count]
    return {"latest_post": latest_post}
