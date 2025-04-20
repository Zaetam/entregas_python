from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionAlumno
from home.models import Alumno
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio (request):
   #return HttpResponse ('<h1>HOLA</h1>')
    return render(request, 'home/inicio.html')

def crear_alumno (request):
    
    if request.method =="POST":
        formulario=CreacionAlumno(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            alumno=Alumno(nombre=info.get('nombre'), curso=info.get('curso'), fecha_creacion=info.get('fecha_creacion'))
            alumno.save()
            return redirect ('listado_de_alumnos')
    else:
        formulario = CreacionAlumno()
    return render(request, 'home/crear_alumno.html',{'formulario': formulario})

def listado_de_alumnos(request):
    alumnos= Alumno.objects.all()
    return render (request, 'home/listado_de_alumnos.html', {'alumnos': alumnos})


def detalle_alumno(request, alumno_en_especifico):
    alumno= Alumno.objects.get(id=alumno_en_especifico)
    return render(request, 'home/detalle_alumno.html', {'alumno':alumno})

class VistaDetalleAlumno(DetailView):
    model =Alumno
    template_name = "home/detalle_alumno.html"

class VistaModificarAlumno(UpdateView):
    model= Alumno
    template_name= "home/modificar_alumno.html"
    fields = ["nombre", "curso", "fecha_creacion"]
    success_url = reverse_lazy('listado_de_alumnos')

class VistaEliminarAlumno(DeleteView):
    model= Alumno
    template_name= "home/eliminar_alumno.html"
    success_url= reverse_lazy('listado_de_alumnos')
