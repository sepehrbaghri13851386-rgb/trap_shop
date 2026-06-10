from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='images/article/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    zaman = models.DateField(default=timezone.now)
class meta:
    ordering = ('zaman,')
    def __str__(self):
        return self.name