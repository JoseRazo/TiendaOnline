from django.contrib import admin
from django.urls import path

from blog.views import inicio

urlpatterns = [
    path('', inicio, name="inicio"),
]
