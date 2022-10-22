import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from blog.models import Category, Post, Comment


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="test", password="testing1234"
    )
    return user


@pytest.fixture
def category():
    ategory = Category.objects.create(name="test_category")
    return ategory


@pytest.fixture
def post(category):
    post = Post.objects.create(
        title = "Test title",
        content = "Test content",
        counted_views = 10,
        status = True,
    )
    post.category.set([category.pk])
    post.save()
    return post


@pytest.mark.django_db
class TestPostsAPI:
    """ Testing blog posts api """
    def test_get_posts_with_unauthorized_user_401_status(self, api_client):
        """ Getting posts with unauthorized user """
        url = reverse("blog:api_v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_create_post_with_unauthorized_user_401_status(self, api_client, category):
        """ Creating a post with unauthorized user """
        url = reverse("blog:api_v1:post-list")
        post = {
            "title" : "Test title",
            "content" : "Test content",
            "category" : category.pk,
            "counted_views" : 10,
            "status" : True,
        }
        response = api_client.post(url, post)
        assert response.status_code == 401

    def test_get_posts_response_200_status(self, api_client, common_user):
        """ Getting posts with authorized user """
        url = reverse("blog:api_v1:post-list")
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_posts_response_201_status(self, api_client, common_user, category):
        """ Creating a post with authorized user """
        url = reverse("blog:api_v1:post-list")
        api_client.force_authenticate(user=common_user)
        post = {
            "title" : "Test post",
            "content" : "Test content",
            "category" : category.pk,
            "counted_views" : 10,
            "status" : True,
        }
        response = api_client.post(url, post)

        created_post = Post.objects.all().last()

        assert response.status_code == 201
        assert created_post.title == "Test post"

    def test_create_post_invalid_data_response_400_status(self, api_client, common_user):
        """ Creating a post with invalid data """
        url = reverse("blog:api_v1:post-list")
        api_client.force_authenticate(user=common_user)
        post = {
            "title" : "Test title",
            "content" : "Test content",
            "counted_views" : 10,
            "status" : True,
        }
        response = api_client.post(url, post)
        assert response.status_code == 400

    def test_edit_posts_response_200_status(self, api_client, common_user, category):
        """ Editing a post with authorized user """
        url = reverse("blog:api_v1:post-list")
        api_client.force_authenticate(user=common_user)
        post = {
            "title" : "Test post",
            "content" : "Test content",
            "category" : category.pk,
            "counted_views" : 10,
            "status" : True,
        }
        # Create the first post
        response = api_client.post(url, post)

        post = {
            "title" : "Test post2",
            "content" : "Test content2",
            "category" : category.pk,
            "counted_views" : 10,
            "status" : True,
        }
        created_post = Post.objects.all().last()
        url = reverse("blog:api_v1:post-detail", kwargs={'pk': created_post.id})
        # Edit the first post
        response = api_client.put(url, post)

        created_post = Post.objects.all().last()

        assert response.status_code == 200
        assert created_post.title == "Test post2"

    def test_delete_posts_response_204_status(self, api_client, common_user, category):
        """ Deleting a post with authorized user """
        url = reverse("blog:api_v1:post-list")
        api_client.force_authenticate(user=common_user)
        post = {
            "title" : "Test post",
            "content" : "Test content",
            "category" : category.pk,
            "counted_views" : 10,
            "status" : True,
        }
        # Create
        response = api_client.post(url, post)

        created_post = Post.objects.all().last()
        url = reverse("blog:api_v1:post-detail", kwargs={'pk': created_post.id})
        # Delete
        response = api_client.delete(url, post)

        assert response.status_code == 204
        assert not Post.objects.filter(title="Test post").exists()


@pytest.mark.django_db
class TestCommentsAPI:
    """ Testing blog comment api """
    def test_get_commnets_with_unauthorized_user_401_status(self, api_client):
        """ Getting posts with unauthorized user """
        url = reverse("blog:api_v1:comment-list")
        response = api_client.get(url)
        assert response.status_code == 401
    
    def test_create_comment_with_unauthorized_user_401_status(self, api_client, post):
        """ Creating a comment with unauthorized user """
        url = reverse("blog:api_v1:comment-list")
        comment = {
            "post" : post.pk,
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment",
            "message" : "This is a test comment",
            "approved" : True,
        }
        response = api_client.post(url, comment)
        assert response.status_code == 401
    
    def test_get_comments_response_200_status(self, api_client, common_user):
        """ Getting comments with authorized user """
        url = reverse("blog:api_v1:comment-list")
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_comment_response_201_status(self, api_client, common_user, post):
        """ Creating a comment with authorized user """
        url = reverse("blog:api_v1:comment-list")
        api_client.force_authenticate(user=common_user)
        comment = {
            "post" : post.pk,
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment",
            "message" : "This is a test comment",
            "approved" : True,
        }
        response = api_client.post(url, comment)

        created_post = Comment.objects.all().last()

        assert response.status_code == 201
        assert created_post.subject == "Test comment"

    def test_create_comment_invalid_data_response_400_status(self, api_client, common_user):
        """ Creating a comment with invalid data """
        url = reverse("blog:api_v1:comment-list")
        api_client.force_authenticate(user=common_user)
        comment = {
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment",
            "message" : "This is a test comment",
            "approved" : True,
        }
        response = api_client.post(url, comment)
        assert response.status_code == 400

    def test_edit_comment_response_200_status(self, api_client, common_user, post):
        """ Editing a comment with authorized user """
        url = reverse("blog:api_v1:comment-list")
        api_client.force_authenticate(user=common_user)
        comment = {
            "post" : post.pk,
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment",
            "message" : "This is a test comment",
            "approved" : True,
        }
        # Create the first post
        response = api_client.post(url, comment)

        comment = {
            "post" : post.pk,
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment2",
            "message" : "This is a test comment",
            "approved" : True,
        }
        created_post = Comment.objects.all().last()
        url = reverse("blog:api_v1:comment-detail", kwargs={'pk': created_post.id})
        # Edit the first post
        response = api_client.put(url, comment)

        created_post = Comment.objects.all().last()

        assert response.status_code == 200
        assert created_post.subject == "Test comment2"

    def test_delete_comment_response_204_status(self, api_client, common_user, post):
        """ Deleting a comment with authorized user """
        url = reverse("blog:api_v1:comment-list")
        api_client.force_authenticate(user=common_user)
        comment = {
            "post" : post.pk,
            "name" : "Test user",
            "email" : "test@gmail.com",
            "subject" : "Test comment",
            "message" : "This is a test comment",
            "approved" : True,
        }
        # Create
        response = api_client.post(url, comment)

        created_post = Comment.objects.all().last()
        url = reverse("blog:api_v1:comment-detail", kwargs={'pk': created_post.id})
        # Delete
        response = api_client.delete(url, comment)

        assert response.status_code == 204
        assert not Comment.objects.filter(subject="Test comment").exists()
