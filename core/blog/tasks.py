from celery import shared_task
from faker import Faker
import random

from django.contrib.auth.models import User
from blog.models import Post, Category

fake = Faker()


@shared_task
def create_new_post():
    # Create a new user
    user, created = User.objects.get_or_create(username=fake.name(), password="Test@123456")

    # Create a new category
    category, created = Category.objects.get_or_create(name="test_category")

    # Create a new posts
    post = Post.objects.create(
        author=user,
        title=fake.text(max_nb_chars=20),
        content=fake.paragraph(nb_sentences=5),
        counted_views=fake.random_int(10, 100),
        status=random.choice([True, False]),
    )
    post.category.set([category.pk])
    post.save()

    return "Post created successfully."
