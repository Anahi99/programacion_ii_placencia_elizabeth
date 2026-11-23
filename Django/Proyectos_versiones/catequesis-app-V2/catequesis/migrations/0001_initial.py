# Generated for Catequesis App v0.2.
import django.conf
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(django.conf.settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Catequista",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombres", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=100)),
                ("cedula", models.CharField(max_length=10, unique=True)),
                ("telefono", models.CharField(max_length=15)),
                ("correo", models.EmailField(max_length=254, unique=True)),
            ],
            options={"verbose_name": "Catequista", "verbose_name_plural": "Catequistas", "ordering": ["apellidos", "nombres"]},
        ),
        migrations.CreateModel(
            name="Participante",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombres", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=100)),
                ("cedula", models.CharField(max_length=10, unique=True)),
                ("fecha_nacimiento", models.DateField()),
                ("representante", models.CharField(max_length=150)),
            ],
            options={"verbose_name": "Participante", "verbose_name_plural": "Participantes", "ordering": ["apellidos", "nombres"]},
        ),
        migrations.CreateModel(
            name="Sacramento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("descripcion", models.TextField(blank=True)),
                ("edad_minima", models.PositiveIntegerField()),
            ],
            options={"verbose_name": "Sacramento", "verbose_name_plural": "Sacramentos", "ordering": ["nombre"]},
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100)),
                ("periodo", models.CharField(max_length=50)),
                ("fecha_inicio", models.DateField()),
                ("fecha_fin", models.DateField()),
                ("cupo", models.PositiveIntegerField()),
                ("estado", models.CharField(choices=[("PLAN", "Planificado"), ("ACT", "Activo"), ("FIN", "Finalizado"), ("CAN", "Cancelado")], default="PLAN", max_length=4)),
                ("catequistas", models.ManyToManyField(blank=True, related_name="cursos", to="catequesis.catequista")),
                ("creado_por", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="cursos_creados", to=django.conf.settings.AUTH_USER_MODEL)),
                ("sacramento", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="cursos", to="catequesis.sacramento")),
            ],
            options={"verbose_name": "Curso", "verbose_name_plural": "Cursos", "ordering": ["-fecha_inicio"]},
        ),
        migrations.CreateModel(
            name="Inscripcion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fecha", models.DateField(auto_now_add=True)),
                ("estado", models.CharField(choices=[("PEN", "Pendiente"), ("CON", "Confirmada"), ("CAN", "Cancelada")], default="PEN", max_length=3)),
                ("creado_por", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="inscripciones_creadas", to=django.conf.settings.AUTH_USER_MODEL)),
                ("curso", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="inscripciones", to="catequesis.curso")),
                ("participante", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="inscripciones", to="catequesis.participante")),
            ],
            options={"verbose_name": "Inscripción", "verbose_name_plural": "Inscripciones", "ordering": ["-fecha"]},
        ),
        migrations.AddConstraint(
            model_name="inscripcion",
            constraint=models.UniqueConstraint(fields=("curso", "participante"), name="inscripcion_unica_por_curso"),
        ),
    ]
