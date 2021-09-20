from django.shortcuts import render
from news.models import Categoria, Noticia

# Create your views here.

def noticias(request):
    noticias = Noticia.objects.filter(status=1).order_by('-created_on')
    categorias = Categoria.objects.all()
    return render(request, "news/noticias.html", {"noticias": noticias, "categorias": categorias})

def noticiaDetalle(request, slug):
    noticia_detalle = Noticia.objects.get(slug=slug)
    categorias = Categoria.objects.all()
    return render(request, "news/noticia_detalle.html", {'noticia_detalle': noticia_detalle, "categorias": categorias})


def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    noticias = Noticia.objects.filter(categoria=categoria, status=1)
    return render(request, "news/categoria.html", {'categoria': categoria, "noticias": noticias, "categorias": categorias})
