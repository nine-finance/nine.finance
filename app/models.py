from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

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


class post(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextUploadingField(null=True, blank=True, external_plugin_resources=(['VideoDetector',
                                                                                        '/staticfiles/ckeditor/ckeditor/plugins/videodetector-master/'
                                                                                        'plugin.js',]),
                                   )
    summary=models.TextField(null=True, blank=True)
    media = models.ImageField(default='background copy.png', upload_to='blog_media')
    date=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



