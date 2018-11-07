from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.Index, name='Home'),
        url(r'^Login.html/', views.Login, name='Login'),
        url(r'^Somos.html/', views.Somos, name='Somos'),
        url(r'^Contacto.html/', views.Contacto, name='Contacto'),
        url(r'^Servicios.html', views.Servicios, name='Servicios'),
        url(r'^Registro.html/$', views.registro, name='Registro'),
        url(r'^Galeria.html/$', views.Galeria, name='Galeria'),
    ]

