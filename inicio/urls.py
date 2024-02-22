from django.urls import path
from inicio.views import  inicio, usuario, crear_usuario

urlpatterns = [
    path('', inicio, name='inicio'),
    path('usuarios/', usuario , name='usuarios'),
    path("crear_usuario/", crear_usuario, name="crear usuario")
    
  ]