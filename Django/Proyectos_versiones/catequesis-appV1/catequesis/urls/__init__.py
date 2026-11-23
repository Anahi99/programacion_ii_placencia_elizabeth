from django.urls import include, path

urlpatterns = [
    path('', include('catequesis.urls.home_urls')),
    path('cuentas/', include('catequesis.urls.auth_urls')),
]
