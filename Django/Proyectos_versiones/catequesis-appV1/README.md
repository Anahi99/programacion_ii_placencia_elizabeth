# Control de Curso de Sacramentos (catequesis-app)

Aplicación web en Django para el control de cursos de sacramentos de la Iglesia Católica.
Sigue la organización por carpetas de `biblioteca-app`: un archivo por entidad en
`models/`, `forms/`, `views/` y `urls/`.

## Versión actual: v0.1 — base del proyecto y autenticación

Incluye: configuración (`config/`), app `catequesis`, registro (con correo), login,
logout por POST, `base.html` con barra de navegación según `user.is_authenticated`,
mensajes y página de inicio protegida con `@login_required`.

## Cómo levantar el proyecto (Visual Studio Code)

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://127.0.0.1:8000/ (redirige al login si no hay sesión).

Base de datos: por defecto sqlite. Para PostgreSQL, editar `.env` con
`DB_ENGINE=postgresql` y los datos de conexión.

## Pruebas

```bash
python manage.py test
```

## Plan de versiones

| Versión | Contenido |
|---|---|
| v0.1 | Config, app, login/registro/logout, base.html y home |
| v0.2 | Modelos (Sacramento, Catequista, Participante, Curso, Inscripcion), admin y migraciones |
| v0.3 | CRUD de Sacramento y Curso |
| v0.4 | CRUD de Inscripción; listado y detalle de Catequista y Participante |
| v0.5 | Grupos, permisos y regla de propiedad |
| v0.6 | Datos de prueba, README con credenciales y CSS opcional |

## Usuarios de prueba

Se documentarán en la v0.6.
