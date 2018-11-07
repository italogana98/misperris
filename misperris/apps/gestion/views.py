from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import Registro


# Create your views here.
def Index(request):
		return render(request, 'Pagina/Index.html', {})

def Login(request):
		return render(request, 'Pagina/Login.html', {})

def Somos(request):
		return render(request, 'Pagina/Somos.html', {})

def Servicios(request):
		return render(request, 'Pagina/Servicios.html', {})

def registro(request):
		form_registro = Registro(request.POST or None)
		variab = {
				"form":form_registro
		}
		if form_registro.is_valid():
				datos = form_registro.cleaned_data
				nombre1 = datos.get("nombre1")
				apellido = datos.get("apellido")
				fechaNac = datos.get("fechaNac")
				usuario = datos.get("usuario") 
				clave = datos.get("clave")
				telefono = datos.get("telefono")
				correo = datos.get("correo")
				db_registro = Usuario(nombre1=nombre1, apellido=apellido, fechaNac=fechaNac, usuario=usuario, clave=clave, telefono=telefono, correo=correo)
				db_registro.save()
		return render(request, 'Pagina/Registro.html', variab)

def Contacto(request):
		return render(request, 'Pagina/Contacto.html', {})

def Galeria(request):
		return render(request, 'Pagina/Galeria.html', {})
