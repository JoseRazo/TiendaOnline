from django.contrib import admin
from django.urls import path

from gestionPedidos.views import contactView, successView, busqueda_productos, buscar

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('busqueda_productos/', busqueda_productos, name='busqueda_productos'),
    path('buscar/', buscar, name='buscar'),
]
