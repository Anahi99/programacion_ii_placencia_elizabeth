from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def inicio(request):
    return HttpResponse(
        "<h1>Catequesis App</h1>"
        "<p>Versión 0.2: modelos y administración.</p>"
        '<p><a href="/admin/">Ir a Django Admin</a></p>'
    )

urlpatterns = [
    path("", inicio, name="home"),
    path("admin/", admin.site.urls),
]
