from django.shortcuts import render, get_object_or_404
from .models import timeline
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    context= {
        "times": timeline.objects.all()
    }
    return render(request, "app/home.html", context )

def preloader(request):
    return render(request, "app/preloader.html")
