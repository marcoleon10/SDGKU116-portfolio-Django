from django.shortcuts import render
from blog.models import BlogPost

def about_view(request):
    posts = BlogPost.objects.all()  # Obtener todos los posts del blog
    return render(request, 'base.html', {'posts': posts})
