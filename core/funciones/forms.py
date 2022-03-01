from django.forms import ModelForm
from funciones import models


class Agregar_Pers(ModelForm):
    class Meta:
        model = models.Persona
        fields = '__all__'

class Agre_puesto(ModelForm):
    class Meta:
        model = models.Puesto
        fields = '__all__'