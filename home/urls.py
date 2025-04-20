from django.urls import path
from home.views import inicio, crear_alumno, listado_de_alumnos, detalle_alumno, VistaDetalleAlumno, VistaModificarAlumno, VistaEliminarAlumno

urlpatterns=[
    path('', inicio, name='inicio' ),
    path('alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
    path('alumnos/crear/', crear_alumno , name='crear_alumno'),
   # path('alumnos/<int:alumno_en_especifico>/', detalle_alumno, name='detalle_alumno'),
    path('alumnos/<int:pk>/', VistaDetalleAlumno.as_view(), name='detalle_alumno'),
    path('alumnos/<int:pk>/modificar/', VistaModificarAlumno.as_view(), name='modificar_alumno'),
    path('alumnos/<int:pk>/eliminar/', VistaEliminarAlumno.as_view(), name='eliminar_alumno'),
]
