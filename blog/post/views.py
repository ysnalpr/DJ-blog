from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views.generic import ListView, DetailView, View
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Post, Category
from .forms import SearchForm


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
        # context["categories"] = Category.objects.all()
        context["category"] = self.category
        return context


class PostDetailView(DetailView):
    template_name = "post/detail.html"

    # def get_queryset(self):

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

        # similar posts
        post_tags_ids = post.tags.values_list("id", flat=True)
        global similar_posts
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
            id=post.id
        )
        similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-publish"
        )[:4]
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["similar_posts"] = similar_posts
        context["absolute_url"] = self.request.build_absolute_uri()
        return context


class SearchView(View):
    def get(self, request):
        form = SearchForm()
        query = None
        results = []
        if "query" in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data["query"]
                search_vector = SearchVector("title", weight="A") + SearchVector(
                    "body", weight="B"
                )
                search_query = SearchQuery(query)
                results = (
                    Post.published.annotate(
                        search=search_vector,
                        rank=SearchRank(search_vector, search_query),
                    )
                    .filter(rank__gte=0.3)
                    .order_by("-rank")
                )
        return render(
            request,
            "post/search.html",
            {
                "form": form,
                "query": query,
                "results": results,
            },
        )
