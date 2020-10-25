from django.db import models
from decimal import Decimal

# Create your models here.

class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=1,null=True)

    class Meta:
        db_table = "categoria"

    def __str__(self):
        return self.descripcion

class marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre =models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=500, null=False)
    
    class Meta:
        db_table = "marca"

    def __str__(self):
        return self.nombre

class producto(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=20,null=True)
    nombre = models.CharField(max_length=100,null=True)
    descripcion_corta = models.CharField(max_length=250,null=True)
    detalle = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    palabras_clave = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=1,null=True)
    imagen = models.ImageField()
    categoria = models.ForeignKey(categoria, on_delete=models.RESTRICT,null=False,blank=False,related_name="FK_productoCategoria")
    marca = models.ForeignKey(marca, on_delete=models.RESTRICT,null=False,blank=False,related_name="FK_productoCategoria")
    
    class Meta:
        db_table = "producto"

class empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=True)
    quienes_somos = models.CharField(max_length=500, null=True)
    email_contacto = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono_contacto = models.CharField(max_length=20, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "empresa"