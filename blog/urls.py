from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('blog/', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail")
]
