
from django.forms import ModelForm
from vista_Clases import models


class CursoForm(ModelForm):
    class Meta:
        model = models.Materia
        fields = '__all__'