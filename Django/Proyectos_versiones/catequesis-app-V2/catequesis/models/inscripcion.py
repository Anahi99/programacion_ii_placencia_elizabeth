from django.conf import settings
from django.db import models
from django.urls import reverse


class Inscripcion(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "PEN", "Pendiente"
        CONFIRMADA = "CON", "Confirmada"
        CANCELADA = "CAN", "Cancelada"

    curso = models.ForeignKey(
        "catequesis.Curso",
        on_delete=models.PROTECT,
        related_name="inscripciones",
    )
    participante = models.ForeignKey(
        "catequesis.Participante",
        on_delete=models.PROTECT,
        related_name="inscripciones",
    )
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=3,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="inscripciones_creadas",
    )

    def __str__(self):
        return f"{self.participante} - {self.curso}"

    def get_absolute_url(self):
        return reverse("inscripcion_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        constraints = [
            models.UniqueConstraint(
                fields=["curso", "participante"],
                name="inscripcion_unica_por_curso",
            )
        ]
