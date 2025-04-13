from django.urls import path
from home.views import inicio, crear_alumno, listado_de_alumnos

urlpatterns=[
    path('', inicio, name='inicio' ),
    path('alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
    path('alumnos/crear/', crear_alumno , name='crear_alumno'),
]