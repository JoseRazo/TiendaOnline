from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Noticia(models.Model):
    titulo=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200, unique=True)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='noticias', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categoria=models.ManyToManyField(Categoria)
    status=models.IntegerField(choices=STATUS, default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='noticia'
        verbose_name_plural='noticias'
        ordering = ['-created_on']


    def __str__(self):
        return self.titulo
