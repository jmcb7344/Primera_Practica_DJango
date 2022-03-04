from datetime import date
from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f'{self.nombre}'

class Estudiante(models.Model):
    SEX_CHOICES = (
        ('M','Hombre'),
        ('F','Mujer')
    )
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField(default=0, null=True, blank=True)
    fec_nac = models.DateField(verbose_name='Fecha de Nacimiento')
    genero = models.CharField(max_length=1, choices=SEX_CHOICES)
    materia = models.ManyToManyField(Materia)

    def edad(self):
        hoy = date.today()
        if (hoy.month, hoy.day) < (self.fec_nac.month, self.fec_nac.day):
            return hoy.year - self.fec_nac.year - 1
        else:
            return hoy.year - self.fec_nac.year

    def __str__(self):
        return f'Estudiante: {self.nombre} {self.apellido}'
   