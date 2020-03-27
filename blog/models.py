from django.db import models
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    summary=models.CharField(max_length=1000, blank=True)
    date=models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
