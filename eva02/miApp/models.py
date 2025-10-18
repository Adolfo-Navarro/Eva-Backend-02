from django.db import models

# Create your models here.
class Producto(models.Model):
    Nombre = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Precio = models.IntegerField()
    Imagen = models.CharField()

    def __str__(self):
        return self.Nombre