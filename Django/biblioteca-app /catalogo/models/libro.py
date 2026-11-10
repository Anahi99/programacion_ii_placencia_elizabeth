from django.db import models
from .categoria import Categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ['titulo']