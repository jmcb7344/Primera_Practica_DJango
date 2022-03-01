from datetime import date
from django.db import models

# Create your models here.
AREA_CHOICES = (
    ('Cal','Calidad'),
    ('Pro','Produccion'),
    ('Adm','Administracion'),
    ('Exp','Expedicion'),
    ('Tec','Tecnica'),
    ('Pos','Postulante'),
)
class Puesto(models.Model):
    puesto = models.CharField(max_length=25)
    area = models.CharField(max_length=3, choices=AREA_CHOICES)
    descripcion = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f'Proceso: {self.area}, Puesto laboral: {self.puesto}'

SEX_CHOICES = (
    ('M','Hombre'),
    ('F','Mujer')
)
class Persona(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField(default=0, null=True, blank=True)
    fec_nac = models.DateField(verbose_name='Fecha de Nacimiento')
    genero = models.CharField(max_length=1, choices=SEX_CHOICES)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, null=False, blank=True)
    activo = models.BooleanField(default=False, verbose_name='Empleador Activo?')

    def edad(self):
        hoy = date.today()
        edad_persona = hoy.year - self.fec_nac.year
        if (hoy.month, hoy.day) < (self.fec_nac.month, self.fec_nac.day):
            return edad_persona - 1
        else:
            return edad_persona

    def __str__(self):
        if self.activo:
            return f'Persona: {self.nombre} {self.apellido} - Area = {self.puesto.area}'
        else:
            return f'Persona: {self.nombre} {self.apellido} - Postulante'
