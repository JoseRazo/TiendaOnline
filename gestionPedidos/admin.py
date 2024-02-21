from django.contrib import admin

from gestionPedidos.models import Cliente, Articulo, Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "telefono")
    search_fields=("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    list_filter=("fecha",)
    date_hierarchy=("fecha")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedido, PedidosAdmin)
