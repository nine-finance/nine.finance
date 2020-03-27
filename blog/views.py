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




    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date')

class PostDetailView(DetailView):
    model= post



