from django.db import models
from decimal import Decimal
from apps.marca.models import marca
from apps.categoria.models import categoria

# Create your models here.

class producto(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=20,null=True)
    nombre = models.CharField(max_length=100,null=True)
    descripcion_corta = models.CharField(max_length=250,null=True)
    detalle = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    palabras_clave = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=1,null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.RESTRICT,null=False,blank=False,related_name="FK_productoCategoria")
    marca = models.ForeignKey(marca, on_delete=models.RESTRICT,null=False,blank=False,related_name="FK_productoCategoria")
    
    class Meta:
        db_table = "producto"