from django.contrib import admin
from .models import Sacramento, Catequista, Participante, Curso, Inscripcion


@admin.register(Sacramento)
class SacramentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "edad_minima")
    list_filter = ("edad_minima",)
    search_fields = ("nombre", "descripcion")


@admin.register(Catequista)
class CatequistaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "cedula", "telefono", "correo")
    list_filter = ("apellidos",)
    search_fields = ("nombres", "apellidos", "cedula", "correo")


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "cedula", "fecha_nacimiento")
    list_filter = ("fecha_nacimiento",)
    search_fields = ("nombres", "apellidos", "cedula", "representante")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "sacramento", "periodo", "fecha_inicio", "estado", "cupo")
    list_filter = ("estado", "periodo", "sacramento")
    search_fields = ("nombre", "periodo")
    filter_horizontal = ("catequistas",)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("id", "participante", "curso", "fecha", "estado", "creado_por")
    list_filter = ("estado", "fecha")
    search_fields = (
        "participante__nombres",
        "participante__apellidos",
        "participante__cedula",
        "curso__nombre",
    )
