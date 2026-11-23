from django.db import models
from django.urls import reverse


class Sacramento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    edad_minima = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("sacramento_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Sacramento"
        verbose_name_plural = "Sacramentos"
