
from django.urls import path

from views.libro_views import (
    create_libro,
    libro_list,
    libro_update,
    libro_delete
)


urlpatterns = [
    path('', libro_list, name='libro_list'),

    path('crear/', create_libro, name='create_libro'),

    path('editar/<int:pk>/', libro_update, name='edit_libro'),

    path('eliminar/<int:pk>/', libro_delete, name='delete_libro'),
]
