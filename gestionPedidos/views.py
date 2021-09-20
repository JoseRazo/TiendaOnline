from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from gestionPedidos.models import Articulo
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from gestionPedidos.forms import ContactForm

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["buscarProducto"]:

        #mensaje="Articulo buscado: %r" %request.GET["buscarProducto"]
        producto=request.GET["buscarProducto"]

        if len(producto)>20:

            mensaje="Texto de busqueda demasiado largo."

        else:

            articulos=Articulo.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:

        mensaje="No haz introducido nada."

    return HttpResponse(mensaje)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['joserrp.13@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
