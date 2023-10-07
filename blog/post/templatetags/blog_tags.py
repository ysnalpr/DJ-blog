from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("post/show_categories.html")
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
