from django import forms

class CreacionAlumno(forms.Form):
    nombre= forms.CharField(max_length=20)
    curso= forms.CharField(max_length=20)
   

