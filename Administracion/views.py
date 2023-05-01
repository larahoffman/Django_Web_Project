from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, 'Administracion/index.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Clientes.objects.filter(nombre__icontains=nombre)
        return render(request, "Administracion/index.html", {"clientes":clientes, "nombre":nombre})
    else:
        respuesta = "Ingrese un nombre"
        return render(request, "Administracion/index.html", {"respuesta":respuesta})


def clientes(request):
    if request.method == 'POST':
        miFormulario = ClientesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            cliente = Clientes(nombre = info['nombre'], correo = info['correo'], telefono = int(info['telefono']))
            cliente.save()
            return render(request, "Administracion/index.html")
    else:
        miFormulario = ClientesFormulario()
        return render(request, "Administracion/clientes.html", {"miFormulario":miFormulario})

def productos(request):
    return render(request, 'Administracion/productos.html')

def pedidos(request):
    return render(request, 'Administracion/pedidos.html')