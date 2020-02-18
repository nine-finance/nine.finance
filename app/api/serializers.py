from rest_framework import serializers
from app.models import timeline

class TimelineSerializer(serializers.ModelSerializer):
    class meta:
        model= timeline
        fields=('title','content', 'date', 'media')

