from django.db import models
from django.utils import timezone

class Blog(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=40,unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=20)
    level = models.CharField(max_length=10, choices=[("beginner", "beginner"), ("intermediate", "intermediate"), ("expert", "expert")])
    language = models.CharField(max_length=30)
    created_date = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title
