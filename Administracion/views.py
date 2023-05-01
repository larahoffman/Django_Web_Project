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
            cliente = Clientes(nombre = info['nombre'], correo = info['correo'], telefono = info['telefono'])
            cliente.save()

            mensaje = "¡Cliente agregado con éxito!"
            miFormulario = ClientesFormulario() #limpio los datos
            return render(request, "Administracion/clientes.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = ClientesFormulario()
        return render(request, "Administracion/clientes.html", {"miFormulario":miFormulario})

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            Producto = Productos(descripcion = info['descripcion'], codigo_producto = info['codigo_producto'])
            Producto.save()

            mensaje = "¡Producto agregado con éxito!"
            miFormulario = ProductosFormulario()
            return render(request, "Administracion/productos.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = ProductosFormulario()
        return render(request, "Administracion/productos.html", {"miFormulario":miFormulario})        

def pedidos(request):
    if request.method == 'POST':
        miFormulario = PedidosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            pedido = Pedidos(numero_pedido = info['numero_pedido'], estado = info['estado'], notas = info['notas'])
            pedido.save()

            mensaje = "¡Pedido agregado con éxito!"
            miFormulario = PedidosFormulario()
            return render(request, "Administracion/pedidos.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = PedidosFormulario()
        return render(request, "Administracion/pedidos.html", {"miFormulario":miFormulario})