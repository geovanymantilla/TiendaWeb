from django.db import models

# Create your models here.

class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=1,null=True)

    class Meta:
        db_table = "categoria"
