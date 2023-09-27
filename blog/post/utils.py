from faker import Faker
import random
from django.contrib.auth.models import User
from taggit.models import Tag
from .models import Post, Category

fake = Faker()


def fake_users(num):
    for _ in range(num):
        user = User.objects.create(
            username=fake.user_name(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
        )
        user.save()


def fake_tags(num):
    for _ in range(num):
        tag = Tag.objects.create(name=fake.unique.word(), slug=fake.unique.slug())
        tag.save()


def fake_categories(num):
    for _ in range(num):
        category = Category.objects.create(
            name=fake.unique.word(), slug=fake.unique.slug()
        )
        category.save()


def fake_posts(num):
    for _ in range(num):
        title = fake.unique.sentence(nb_words=10)
        slug = fake.unique.slug()
        body = fake.paragraph(nb_sentences=10)
        user_id = random.randint(1, 100)
        user = User.objects.get(id=user_id)
        category_id = random.randint(1, 20)
        category = Category.objects.get(id=category_id)
        tag_id = random.randint(1, 500)
        tag = Tag.objects.get(id=tag_id)
        status = fake.random_choices(elements=("DF", "PB"))
        published = fake.unique.past_datetime()
        created = fake.unique.past_datetime()
        updated = fake.unique.past_datetime()

        post = Post.objects.create(
            title=title,
            slug=slug,
            body=body,
            author=user,
            category=category,
            tags=tag,
            status=status,
            publish=published,
            created=created,
            updated=updated,
        )
        post.save()
