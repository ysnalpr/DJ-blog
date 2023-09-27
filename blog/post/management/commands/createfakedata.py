from django.core.management.base import BaseCommand
from post.utils import fake_users, fake_tags, fake_categories, fake_posts


class Command(BaseCommand):
    help = "Use this command for generating fake data for your models."

    def handle(self, *args, **options):
        fake_users(100)
        print("Users created")
        fake_tags(500)
        print("Tags created")
        fake_categories(20)
        print("Categories created")
        fake_posts(500)
        print("Completed")
