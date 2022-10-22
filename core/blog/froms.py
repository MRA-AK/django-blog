from django import forms

from blog.models import Post, Comment


class PostUpdateForm(forms.ModelForm):
    """
    Form for editing a post.
    """

    class Meta:
        model = Post
        exclude = ['author', ]


class CommentForm(forms.ModelForm):
    """
    Form for creating a comment.
    """

    class Meta:
        model = Comment
        fields = ['email', 'subject', 'message']
