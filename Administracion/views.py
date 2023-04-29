from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, 'Administracion/index.html')

def clientes(request):
    return render(request, 'Administracion/clientes.html')

def productos(request):
    return render(request, 'Administracion/productos.html')

def pedidos(request):
    return render(request, 'Administracion/pedidos.html')