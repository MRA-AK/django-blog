from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from blog.models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from .paginations import PostPagination


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['author', 'category', 'status']
    search_fields = ['title', 'content']
    # pagination_class = PostPagination

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.all()
