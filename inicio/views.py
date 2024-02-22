from django.shortcuts import render, redirect
from inicio.models import Usuario 
from inicio.forms import CreacionUsuarioForm

def inicio(request): 
  
    usuario = Usuario.objects.all()
    return render(request, "inicio.html", {})

def usuario(request):
    usuario = Usuario.objects.all()
    return render(request, "usuario.html", {"usuario": usuario})

#def crear_cliente(request, nombre,apellido, edad):
 #   cliente = Cliente (nombre=nombre, apellido=apellido, edad=edad, dinero_gastado=random.randint(1,100))
 #   cliente.save() 
 #   return render(request, "crear_cliente.html", {"cliente":cliente})

def crear_usuario(request):
    form = CreacionUsuarioForm()
    if request.method == "POST":
        form = CreacionUsuarioForm(request.POST)
        return redirect("forms/crear_usuario/")   
    return render(request, "crear_usuario.html", {})
