from django.urls import path
from .views import test_view, about_view

urlpatterns = [
    path('testing', test_view, name="test"),
    path("", about_view, name="about"),
]