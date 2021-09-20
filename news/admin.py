from django.contrib import admin

from .models import Categoria, Noticia

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created_on', 'updated_on')

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields=('created_on', 'updated_on')
    list_display = ('titulo', 'slug', 'autor', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
