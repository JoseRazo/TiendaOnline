from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm

# Create your views here.

def contactView(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            asunto = request.POST.get('asunto')
            mensaje = request.POST.get('mensaje')

            email=EmailMessage("Mensaje desde el formulario de contacto.",
            "El usuario {} con correo electronico {} escribe lo siguiente:\n\n Asunto: {}\n\n {}".format(nombre, email, asunto, mensaje),
            "", ["joserrp.13@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?valido')
            except Exception as e:
                return redirect('/contacto/?novalido')

    return render(request, "contacto/contacto.html", {'miFormulario': form})
