from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from datetime import date

from .models import Sacramento, Catequista, Participante, Curso, Inscripcion


class ModelosCatequesisTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="prueba",
            password="ClaveTemporal123!",
        )
        self.sacramento = Sacramento.objects.create(
            nombre="Primera Comunión",
            descripcion="Preparación para la primera comunión",
            edad_minima=9,
        )
        self.catequista = Catequista.objects.create(
            nombres="Ana",
            apellidos="Pérez",
            cedula="0102030405",
            telefono="0991234567",
            correo="ana@example.com",
        )
        self.participante = Participante.objects.create(
            nombres="Luis",
            apellidos="Gómez",
            cedula="0102030406",
            fecha_nacimiento=date(2015, 5, 10),
            representante="María Gómez",
        )
        self.curso = Curso.objects.create(
            sacramento=self.sacramento,
            nombre="Primera Comunión 2026",
            periodo="2026",
            fecha_inicio=date(2026, 1, 10),
            fecha_fin=date(2026, 6, 10),
            cupo=25,
            creado_por=self.usuario,
        )
        self.curso.catequistas.add(self.catequista)

    def test_relacion_curso_catequista(self):
        self.assertIn(self.catequista, self.curso.catequistas.all())

    def test_crear_inscripcion(self):
        inscripcion = Inscripcion.objects.create(
            curso=self.curso,
            participante=self.participante,
            creado_por=self.usuario,
        )
        self.assertEqual(inscripcion.estado, Inscripcion.Estado.PENDIENTE)

    def test_no_permite_inscripcion_duplicada(self):
        Inscripcion.objects.create(
            curso=self.curso,
            participante=self.participante,
            creado_por=self.usuario,
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Inscripcion.objects.create(
                    curso=self.curso,
                    participante=self.participante,
                    creado_por=self.usuario,
                )
