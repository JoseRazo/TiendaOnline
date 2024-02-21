from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="Dirección")
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=10, verbose_name="Teléfono")

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es: %s la sección es: %s y el precio es: %s' % (self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
