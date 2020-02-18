from rest_framework.generics import ListAPIView, RetrieveAPIView
from app.views import times
from .serializers import TimelineSerializer

class TimelineListView(ListAPIView):
    queryset = times.objects.all()
    serializer_class = TimelineSerializer

class TimelineDetailView(RetrieveAPIView):
    queryset = times.objects.all()
    serializer_class = TimelineSerializer
