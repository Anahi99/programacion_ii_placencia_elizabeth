from django.db import models
from django.urls import reverse


class Participante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    representante = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def get_absolute_url(self):
        return reverse("participante_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["apellidos", "nombres"]
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
