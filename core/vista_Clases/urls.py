from unicodedata import name
from django.urls import path
from vista_Clases import views


app_name = 'clases'

urlpatterns = [
    path('', views.HomesClass.as_view(), name='home'),
    path('nuevo', views.NuevasPersona.as_view(), name='nuevo'),
    path('detalle/<int:pk>/', views.DetallePersona.as_view(), name='detalle'),
    path('eliminar/<int:pk>/', views.EliminarPersona.as_view(), name='eliminar'),
    path('editar/<int:pk>/', views.EditarPersona.as_view(), name='editar' ),
    path('cursos/', views.HomeCurso.as_view(), name='curso'),
    path('nuevocurso/', views.AgregarCurso.as_view(), name='nuevocurso'),
    path('editarCurso/<int:pk>/', views.EditarCurso.as_view(), name='editarCurso'),
]