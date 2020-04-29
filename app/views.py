from django.shortcuts import render
from .models import timeline
from django.views.generic import ListView, DetailView
from .models import post, post1

def home(request):
    context= {
        "times": timeline.objects.all(),
        "posts": post.objects.all()
    }
    return render(request, "app/home.html", context)

def preloader(request):
    return render(request, "app/preloader.html")

def blog(request):
    context={
        "posts1": post1.objects.all()
    }
    return render(request, "app/blog.html", context)

class PostListView(ListView):
    model = post
    template_name = 'app/home.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostListView1(ListView):
    model = post1
    template_name = 'app/blog.html'
    context_object_name = 'posts1'
    ordering = ['-date']

class PostDetailView(DetailView):
    model= post

class PostDetailView1(DetailView):
    model= post1
