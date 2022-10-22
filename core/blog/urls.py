from django.urls import path, include
from blog.views import PostDetailView, PostListView, PostUpdateView, PostDeleteView, PostFilterCateforyView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path('index/', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetailView.as_view(), name='single'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('category/<str:cat_name>/', PostFilterCateforyView.as_view(), name='category'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path("api/v1/", include("blog.api.v1.urls")),
]
