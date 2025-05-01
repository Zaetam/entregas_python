from django import forms

class CreacionAlumno(forms.Form):
    nombre= forms.CharField(max_length=20)
    curso= forms.CharField(max_length=20)
    fecha_creacion=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    imagen = forms.ImageField(required=False)
   

