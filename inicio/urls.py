# inicio/urls.py
from django.urls import path
from .views import landing, ProyectoList, ProyectoCreate, ProyectoUpdate, ProyectoDelete


urlpatterns = [
    path('', landing, name='landing'),
    path("proyectos/", ProyectoList.as_view(), name="proyecto_list"),
    path("proyectos/nuevo/", ProyectoCreate.as_view(), name="proyecto_create"),
    path("proyectos/<int:pk>/editar/", ProyectoUpdate.as_view(), name="proyecto_update"),
    path("proyectos/<int:pk>/eliminar/", ProyectoDelete.as_view(), name="proyecto_delete"),
]
