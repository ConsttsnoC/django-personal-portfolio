from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-data')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


