from django.contrib import admin
from .models import marca
# Register your models here.

class listarMarca(admin.ModelAdmin):
    list_display= [
        "id", "nombre","descripcion"
    ]
admin.site.register(marca, listarMarca)


