from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Ingresa tu nombre', min_length=3, max_length=100, required=True)
    email = forms.EmailField(label='Ingresa tu email', required=True)
    asunto = forms.CharField(label='Ingresa tu asunto', max_length=100, required=True)
    mensaje = forms.CharField(label='Ingresa tu mensaje', widget=forms.Textarea, required=True)
