from django.urls import path
from . import views

urlpatterns = [
    path('', views.preloader, name="app-preloader"),
    path('home/', views.home, name="app-home"),
    path('home/', views.PostListView.as_view(), name="blog-homepage"),
    path('blog/', views.blog, name="blog-more"),
    path('blog/', views.PostListView1.as_view(), name="blog-home"),
    path('blog2/', views.blog2, name="blog2-more"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post1/<int:pk>/', views.PostDetailView1.as_view(), name="blogpost-detail"),
]
