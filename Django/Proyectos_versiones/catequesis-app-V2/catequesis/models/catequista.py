from django.db import models
from django.urls import reverse


class Catequista(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def get_absolute_url(self):
        return reverse("catequista_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["apellidos", "nombres"]
        verbose_name = "Catequista"
        verbose_name_plural = "Catequistas"
