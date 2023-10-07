from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "publish", "status"]
    list_filter = ["status", "publish", "created", "author"]
    list_editable = ["status"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


admin.site.register(
    Category,
    MPTTModelAdmin,
    list_display=["name"],
)

# @admin.register(Category)
# class CategoryAdmin(DraggableMPTTAdmin):
#     list_display = ["name", "slug", "parent"]
#     list_display_links = ["name"]
#     list_filter = ["parent"]
#     search_fields = ["name"]
#     prepopulated_fields = {"slug": ("name",)}
