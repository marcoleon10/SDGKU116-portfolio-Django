from django.urls import path
from . import views

urlpatterns = [
    path('like/<str:section>/', views.like_section, name='like_section'),
    path('dislike/<str:section>/', views.dislike_section, name='dislike_section'),
]
