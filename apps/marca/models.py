from django.db import models

# Create your models here.


class marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre =models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=500, null=False)
    
    class Meta:
        db_table = "marca"

    def __str__(self):
        return self.nombre


