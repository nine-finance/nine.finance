from django.urls import path
from .views import TimelineListView, TimelineDetailView

urlpatterns = [
    path('',TimelineListView.as_view()),
    path('<pk>', TimelineDetailView.as_view())

]

