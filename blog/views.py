# views.py

from django.shortcuts import render
from .models import BlogPost

def lista_posts(request):
    posts = BlogPost.objects.all()  # Obtener todos los posts
    return render(request, 'blog/new_blog_post.html', {'posts': posts})
