from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100) #maximo son 100 caracteres
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #

    def __str__(self):
        return self.name

#curso sacramento iglesia catolica

class Sacramento(models.Model):
    name = models.CharField(max_length=100) #maximo son 100 caracteres
    tipo_sacramento = models.TextField(blank=True)
    asistiencia = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #hacer auditoria de como se creo el registro

    def __str__(self):
        return self.name
