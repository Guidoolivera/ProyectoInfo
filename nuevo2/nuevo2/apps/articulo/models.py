from typing import Any, Dict, Tuple
from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=30,null=False)
    
    def __str__(self):
        return self.nombre

#articulos = []
class Articulo(models.Model):

    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría.')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)  

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
