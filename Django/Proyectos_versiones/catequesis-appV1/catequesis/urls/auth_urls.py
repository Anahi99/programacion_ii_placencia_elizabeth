from django.urls import path

from catequesis.views import login_view, logout_view, registro_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_view, name='registro'),
]
