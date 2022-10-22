from django.contrib import admin
from blog.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Show Category model in django admin panel.
    """
    # list_display = []
    # search_fields = 
    # list_filter =


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Show Post model in django admin panel.
    """
    # list_display = []
    # search_fields = 
    # list_filter = 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Show Comment model in django admin panel.
    """
    # list_display = []
    # search_fields = 
    # list_filter = 
