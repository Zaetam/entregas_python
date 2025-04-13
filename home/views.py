from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionAlumno
from home.models import Alumno

# Create your views here.
def inicio (request):
   #return HttpResponse ('<h1>HOLA</h1>')
    return render(request, 'home/inicio.html')

def crear_alumno (request):
    
    if request.method =="POST":
        formulario=CreacionAlumno(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            alumno=Alumno(nombre=info.get('nombre'), curso=info.get('curso'))
            alumno.save()
            return redirect ('listado_de_alumnos')
    else:
        formulario = CreacionAlumno()
    return render(request, 'home/crear_alumno.html',{'formulario': formulario})

def listado_de_alumnos(request):
    alumnos= Alumno.objects.all()
    return render (request, 'home/listado_de_alumnos.html', {'alumnos': alumnos})
