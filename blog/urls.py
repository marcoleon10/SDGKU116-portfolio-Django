# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    # Otros patrones de URL de la aplicación blog
]
