from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.noticias, name="noticias"),
    path('<slug:slug>/', views.noticiaDetalle, name="noticia_detalle"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]
