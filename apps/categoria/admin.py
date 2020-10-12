from django.contrib import admin
from .models import categoria

class listarCategoria(admin.ModelAdmin):
    list_display= [
        "id", "descripcion", "estado"
    ]

admin.site.register(categoria,listarCategoria)
# Register your models here.

