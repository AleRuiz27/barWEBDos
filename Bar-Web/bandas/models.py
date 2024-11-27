from django.db import models

# Create your models here.
class conciertos(models.Model):
    ARTISTAS = models.CharField(max_length=100)
    LUGAR = models.CharField(max_length=100)
    FECHA = models.DateField()
    def __str__(self):
        return self.ARTISTAS
    

class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()