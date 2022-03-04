from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from vista_Clases import models, forms

# Create your views here.
class HomesClass(generic.ListView):
    model = models.Estudiante
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        contar = models.Estudiante.objects.count()
        context = super(HomesClass, self).get_context_data(**kwargs)
        context['titulo'] = 'Listado de alumnos'
        context['contar'] = contar
        return context

class DetallePersona(generic.DetailView):
    model = models.Estudiante

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Detalle persona'
        return context

class NuevasPersona(generic.CreateView):
    model = models.Estudiante
    fields = '__all__'
    success_url = reverse_lazy('clases:home')

class EliminarPersona(generic.DeleteView):
    model = models.Estudiante
    success_url = reverse_lazy('clases:home')

class EditarPersona(generic.UpdateView):
    model = models.Estudiante
    fields = '__all__'
    success_url = reverse_lazy('clases:home')

class HomeCurso(generic.View):
    model = models.Materia
    def get(self, request, *args, **kwargs):
        context = {
            'curso': self.model.objects.all(),
            'titulo': 'Cursos',
            'contar': self.model.objects.count(),
        }
        return render(request, 'home_curso.html', context)

class AgregarCurso(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registro_curso.html', {'form': forms.CursoForm})

    def post(self, request, *args, **kwargs):
        form = forms.CursoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('clases:curso')

class EditarCurso(generic.View):
    def get(self, request, pk, *args, **kwargs):
        curso = get_object_or_404(models.Materia, pk=pk)
        return render(request, 'registro_curso.html', {'form': forms.CursoForm(instance=curso)})

    def post(self, request, pk, *args, **kwargs):
        curso = get_object_or_404(models.Materia, pk=pk)
        form = forms.CursoForm(request.POST, instance=curso)
        if form.is_valid:
            form.save()
        return redirect('clases:curso')

