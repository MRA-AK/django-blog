from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, CommentViewSet

app_name = 'api_v1'

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('category', CategoryViewSet, basename='category')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls), name='blog-api'),
]
