from django.db import models
from django.utils import timezone


class Carousel(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Skill(models.Model):
    icon = models.CharField(max_length=10)
    name= models.CharField(max_length=10)
    body = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name