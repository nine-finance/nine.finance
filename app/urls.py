from django.urls import path
from . import views

urlpatterns = [
    path('', views.preloader, name="app-preloader"),
    path('home/', views.home, name="app-home"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail")
]
