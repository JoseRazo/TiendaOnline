from django.contrib import admin

from servicios.models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display=("titulo", "contenido", "imagen", "created")
    readonly_fields=("created", "updated")

admin.site.register(Servicio, ServicioAdmin)
