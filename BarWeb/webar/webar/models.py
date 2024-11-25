from django.db import models
class Personas(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)