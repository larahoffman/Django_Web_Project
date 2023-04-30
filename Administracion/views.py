from django.shortcuts import render
from .models import *
# Create your views here.

def inicio(request):
    return render(request, 'Administracion/index.html')

def clientes(request):
    if request.method == 'post':
        cliente = Clientes(request.POST['nombre'], request.POST['correo'], int(request.POST['telefono'])) # deberia pasarle el id?
        cliente.save()
        return render(request, "Administracion/index.html")
    return render(request, 'Administracion/clientes.html')

def productos(request):
    return render(request, 'Administracion/productos.html')

def pedidos(request):
    return render(request, 'Administracion/pedidos.html')