from django.db import models

# Create your models here.

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