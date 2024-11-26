from django.db import models
class Evento(models.Model):
    banda = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    dia = models.DateField()
    def __str__(self):
        return self.banda