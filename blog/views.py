from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import post


def blog(request):
    context = {
        "posts": post.objects.all()
    }
    return render(request, "blog/home.html", context )

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model= post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'



