from django.db import models

class timeline(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    media = models.ImageField(upload_to='timeline_media')
    position = models.TextField(default='1st', editable=True)

    def __str__(self):
        return self.title






