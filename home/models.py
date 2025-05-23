from django.db import models 

class Alumno(models.Model):
    nombre= models.CharField(max_length=20)
    curso= models.CharField(max_length=20)
    fecha_creacion= models.DateField(null=True)
    imagen = models.ImageField( upload_to="imagenes", null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.curso}'