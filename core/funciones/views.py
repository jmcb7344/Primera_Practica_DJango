<<<<<<< HEAD
from django.shortcuts import get_object_or_404, redirect, render
from funciones import models, forms
=======
from django.shortcuts import render
from funciones import models
>>>>>>> 1132b57 (b)

# Create your views here.
def home(request):
    context = {
        'titulo':'Paguina principal',
<<<<<<< HEAD
        'personas': models.Persona.objects.order_by(),
        'contar': models.Persona.objects.count(),
        'activo':models.Persona.objects.filter(activo=True).count(),
    }
    return render(request, 'home_fun.html', context)

def detalle(request, id):
    return render(request, 'detalle.html', {'persona': get_object_or_404(models.Persona, pk=id)})

def editar(request, id):
    pers = get_object_or_404(models.Persona, pk=id)
    if request.method == 'POST':
        persForm = forms.Agregar_Pers(request.POST, instance=pers)
        if persForm.is_valid:
            persForm.save()
            return redirect('fun:home')
    else:
        return render(request, 'registro_persona.html', {'persForm': forms.Agregar_Pers(instance=pers)})

def eliminar(request, id):
    pers = models.Persona.objects.get(pk=id)
    if pers:
        pers.delete()
    return redirect('fun:home')

def agregar(request):
    if request.method == 'POST':
        persForm = forms.Agregar_Pers(request.POST)
        if persForm.is_valid:
            persForm.save()
            return redirect('fun:home')
    else:
        return render(request, 'registro_persona.html', {'persForm': forms.Agregar_Pers} )
    
def agregar_puesto(request):
    if request.method == 'POST':
        puesto = forms.Agre_puesto(request.POST)
        if puesto.is_valid:
            puesto.save()
            return redirect('fun:home')
    else:
        return render(request, 'registro_puesto.html', {'pue': forms.Agre_puesto})

def detalle_Puesto(request, id):
    return render(request, 'detallePuesto.html', {'pue': get_object_or_404(models.Puesto, pk=id)})

def puestos(request):
    context = {
        'puesto': models.Puesto.objects.order_by(),
        'contar': models.Puesto.objects.count(),
    }
    return render(request, 'home_puesto.html', context)

def editar_puesto(request, id):
    puesto = get_object_or_404(models.Puesto, pk=id)
    if request.method == 'POST':
        pue = forms.Agre_puesto(request.POST, instance=puesto)
        if pue.is_valid:
            pue.save()
            return redirect('fun:puesto')
    else:
        return render(request, 'registro_puesto.html', {'pue': forms.Agre_puesto(instance=puesto)})

def eliminar_puesto(request, id):
    puesto = get_object_or_404(models.Puesto, pk=id)
    if puesto:
        puesto.delete()
    return redirect('fun:puesto')
=======
        'personas': models.Persona.objects.all()
    }
    return render(request, 'home_fun.html', context)

def detalle(request):
    pass

def editar(request):
    pass

def eliminar(request):
    pass
>>>>>>> 1132b57 (b)
