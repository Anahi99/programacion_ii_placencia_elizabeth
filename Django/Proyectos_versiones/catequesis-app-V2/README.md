# Catequesis App — versión 0.2

Proyecto Django para administrar sacramentos, catequistas, participantes, cursos e inscripciones.

## Requisitos
- Python 3.10 o superior (recomendado: la misma versión usada en clase).
- Django 6.1.x.

## 1. Preparar el entorno

Desde la carpeta `catequesis-app`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows, activa el entorno con:
```bash
.venv\Scripts\activate
```

## 2. Configuración

Copia `.env.example` a `.env` y cambia `SECRET_KEY` por una clave propia.
La configuración actual lee las variables del entorno si están definidas; el proyecto funciona también con los valores de desarrollo incluidos.

## 3. Base de datos y migraciones

```bash
python manage.py makemigrations catequesis
python manage.py migrate
python manage.py check
```

La carpeta `catequesis/migrations` incluye la migración inicial. Si Django indica que no hay cambios pendientes, puedes continuar.

## 4. Crear usuario administrador

```bash
python manage.py createsuperuser
```

## 5. Ejecutar

```bash
python manage.py runserver
```

Abre:
- Página inicial: http://127.0.0.1:8000/
- Administración: http://127.0.0.1:8000/admin/

## Modelos incluidos
1. Sacramento
2. Catequista
3. Participante
4. Curso
5. Inscripcion

## Relaciones
- Curso → Sacramento: ForeignKey con `PROTECT`.
- Curso ↔ Catequista: ManyToManyField.
- Inscripcion → Curso: ForeignKey con `PROTECT`.
- Inscripcion → Participante: ForeignKey con `PROTECT`.
- Curso e Inscripcion → usuario creador: ForeignKey al modelo de usuario configurado en Django.

La restricción `inscripcion_unica_por_curso` evita duplicar la inscripción de una misma persona en un mismo curso.

## Alcance de esta versión
Esta entrega corresponde a la v0.2: modelos, administración y migraciones. Los CRUD públicos, las URLs de detalle, los permisos por grupos y la carga de datos de prueba se desarrollan en versiones posteriores.

**Nota:** `get_absolute_url()` ya apunta a los nombres de rutas previstos para la v0.3. Es normal que esas rutas todavía no estén implementadas en esta versión.
