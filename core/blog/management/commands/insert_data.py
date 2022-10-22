from django.core.management.base import BaseCommand

from faker import Faker
import random

from django.contrib.auth.models import User
from blog.models import Post, Category, Comment


class Command(BaseCommand):
    help = "creating five dummy posts"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # Create a new user
        user, created = User.objects.get_or_create(username=self.fake.name(), password="Test@123456")

        # Create a new category
        category, created = Category.objects.get_or_create(name="test_category")

        for _ in range(5):
            # Create five dummy posts
            post = Post.objects.create(
                author = user,
                title = self.fake.text(max_nb_chars=20),
                content = self.fake.paragraph(nb_sentences=5),
                counted_views = self.fake.random_int(10, 100),
                status = random.choice([True, False]),
            )
            post.category.set([category.pk])
            post.save()
        print("5 dummy posts created successfully. \U0001F642")
