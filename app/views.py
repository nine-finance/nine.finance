from django.shortcuts import render
from .models import timeline
from django.views.generic import ListView, DetailView
from .models import post

def home(request):
    context= {
        "times": timeline.objects.all()
    }
    return render(request, "app/home.html", context )

def preloader(request):
    return render(request, "app/preloader.html")

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
