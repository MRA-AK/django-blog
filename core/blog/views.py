from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from blog.models import Post, Comment, Category
from blog.froms import PostUpdateForm, CommentForm


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog-home.html"

    def get_queryset(self):
        return self.model.objects.filter(status=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=context["post"].pk, approved=True)
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("blog:index")
    form_class = PostUpdateForm
    template_name = "blog/blog-single-edit.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("blog:index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PostFilterCateforyView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog-home.html"

    def get_queryset(self):
        category = Category.objects.filter(name__iexact=self.kwargs["cat_name"]).last()
        return Post.objects.filter(category=category, status=True)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "blog/blog-comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.instance.post_id = self.kwargs["pk"]
        form.instance.approved = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:single', kwargs={'pk': self.kwargs["pk"]})
