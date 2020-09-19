from django.urls import path
from . import views

urlpatterns = [
    path('', views.preloader, name="app-preloader"),
    path('home/', views.home, name="app-home"),
    path('home/', views.PostListView.as_view(), name="blog-homepage"),
    path('blog/', views.blog, name="blog-more"),
    path('blog/', views.PostListView1.as_view(), name="blog-home"),
    path('blog2/', views.blog2, name="blog2-more"),
    path('blog3/', views.blog3, name="blog3-more"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post1/<int:pk>/', views.PostDetailView1.as_view(), name="blogpost-detail"),
    path('post2/<int:pk>/', views.PostDetailView2.as_view(), name="blogpost2-detail"),
    path('post3/<int:pk>/', views.PostDetailView3.as_view(), name="blogpost3-detail"),
]
