from django.contrib import admin
from .models import Message, Carousel, Skill
# Register your models here.
admin.site.register(Carousel)
admin.site.register(Skill)
admin.site.register(Message)