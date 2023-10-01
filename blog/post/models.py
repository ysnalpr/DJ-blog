from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(verbose_name="Title", max_length=250, unique=True)
    slug = models.SlugField(
        max_length=250, unique_for_date="publish", allow_unicode=True
    )
    body = RichTextField(verbose_name="Body")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="author",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        "Category", related_name="posts", on_delete=models.CASCADE
    )
    tags = TaggableManager()
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    parent = TreeForeignKey(
        "self", blank=True, null=True, related_name="child", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        unique_together = (
            "slug",
            "parent",
        )

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return "->".join(full_path[::-1])

    def get_absolute_url(self):
        return reverse("post:post_list_by_category", args=[self.slug])
