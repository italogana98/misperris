from django import forms
from .models import Usuario
from .models import Contacto

class Registro  (forms.Form):
    nombre1 = forms.CharField(max_length=35)
    apellido = forms.CharField(max_length=35)
    fechaNac = forms.DateField()
    usuario = forms.CharField(max_length=35)
    clave = forms.CharField(max_length=35)
    telefono = forms.CharField(max_length=35)
    correo = forms.CharField(max_length=35)