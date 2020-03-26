from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def blog_index(request):
    print("Index triggered")
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {"blogs":blogs[:4]})