from django.contrib import admin
from blog.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Show Category model in django admin panel.
    """
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Show Post model in django admin panel.
    """
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Show Comment model in django admin panel.
    """
    pass
