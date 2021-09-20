from django.contrib import admin

from .models import CategoriaProducto, Producto

# Register your models here.

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    list_display = ('nombre', 'created_on')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    list_display = ('nombre', 'categorias', 'imagen', 'precio', 'disponibilidad', 'created_on')
    list_filter = ("categorias",)
    search_fields = ['nombre', 'categorias']

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
