from django.conf import settings
from django.db import models
from django.urls import reverse


class Curso(models.Model):
    class Estado(models.TextChoices):
        PLANIFICADO = "PLAN", "Planificado"
        ACTIVO = "ACT", "Activo"
        FINALIZADO = "FIN", "Finalizado"
        CANCELADO = "CAN", "Cancelado"

    sacramento = models.ForeignKey(
        "catequesis.Sacramento",
        on_delete=models.PROTECT,
        related_name="cursos",
    )
    catequistas = models.ManyToManyField(
        "catequesis.Catequista",
        related_name="cursos",
        blank=True,
    )
    nombre = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupo = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=4,
        choices=Estado.choices,
        default=Estado.PLANIFICADO,
    )
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="cursos_creados",
    )

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("curso_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-fecha_inicio"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
