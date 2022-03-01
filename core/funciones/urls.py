from django.urls import path
from funciones import views

app_name = 'fun'

urlpatterns = [
    path('', views.home, name='home'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('agregar/', views.agregar, name='agregar'),
    path('agregar_puesto/', views.agregar_puesto, name='agregar_puesto'),
    path('detalle_Puesto/<int:id>', views.detalle_Puesto, name='detalle_Puesto'),
    path('puesto/', views.puestos, name='puesto'),
    path('editar_puesto/<int:id>', views.editar_puesto, name='editar_puesto'),
    path('eliminar_puesto/<int:id>', views.eliminar_puesto, name='eliminar_puesto'),
]