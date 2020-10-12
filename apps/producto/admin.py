from django.contrib import admin
from .models import producto
# Register your models here.

class listarProducto(admin.ModelAdmin):
    list_display= [
        "id", "referencia", "nombre","valor","estado", "categoria","marca"
    ]

admin.site.register(producto, listarProducto)