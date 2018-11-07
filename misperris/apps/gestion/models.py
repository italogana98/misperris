from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Usuario  (models.Model):
    nombre1 = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    fechaNac = models.DateField(default=datetime.now)
    usuario = models.CharField(max_length=35)
    clave = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    correo = models.CharField(max_length=35,default='a')

    def nombreCompleto(self):
        cadena="{0} {1}"
        return cadena.format(self.apellido, self.nombre1)

    def __str__(self):
        return self.nombreCompleto()

class Contacto (models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    empresa = models.CharField(max_length=35)
    correo = models.CharField(max_length=35,default='a')
    descripcion = models.CharField(max_length=100)

class Perro(models.Model):
    Nombre_perro = models.CharField(max_length=30)
    Raza = models.CharField(max_length=50)
    Descripcion_perro = models.CharField(max_length=150)
    Estado = models.IntegerField()