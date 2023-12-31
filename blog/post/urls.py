from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = "post"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "category/<slug:category_slug>/",
        views.PostListView.as_view(),
        name="post_list_by_category",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path("search/", views.SearchView.as_view(), name="post_search"),
    path("feed/", LatestPostsFeed(), name="post_feed"),
]
