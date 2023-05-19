from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, 'AppFinal/index.html')

# def leerProductos(request):
#     productos = Productos.objects.all()
#     context = {"productos":productos}
#     return render(request, "AppFinal/leerProductos.html", context)

class ProductosList(ListView):
    model = Productos
    template_name = "AppFinal/productos_list.html"

class ProductosDetail(DetailView):
    model = Productos
    template_name = "AppFinal/productos_detalle.html"

class ProductosCreate(CreateView):
    model = Productos
    template_name = "AppFinal/productos_create.html"
    success_url = "/productos/list"
    fields = '__all__'

class ProductosUpdate(UpdateView):
    model = Productos
    success_url = "/productos/list"
    fields = '__all__'

class ProductosDelete(DeleteView):
    model = Productos
    success_url = "/productos/list"

def leerMensajes(request):
    mensajes = Mensajes.objects.all()
    context = {"mensajes":mensajes}
    return render(request, "AppFinal/leerMensajes.html", context)


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Productos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFinal/index.html", {"productos":productos, "nombre":nombre})
    else:
        respuesta = "Ingrese un nombre"
        return render(request, "AppFinal/index.html", {"respuesta":respuesta})


# def usuarios(request):
#     if request.method == 'POST':
#         miFormulario = ClientesFormulario(request.POST)
#         print(miFormulario)

#         if miFormulario.is_valid:
#             info = miFormulario.cleaned_data
#             cliente = Clientes(nombre = info['nombre'], correo = info['correo'], telefono = info['telefono'])
#             cliente.save()

#             mensaje = "¡Cliente agregado con éxito!"
#             miFormulario = ClientesFormulario() #limpio los datos
#             return render(request, "AppFinal/clientes.html", {"miFormulario":miFormulario, "mensaje":mensaje})
#     else:
#         miFormulario = ClientesFormulario()
#         return render(request, "AppFinal/clientes.html", {"miFormulario":miFormulario})

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            Producto = Productos(nombre = info['nombre'], categoria = info['categoria'], descripcion = info['descripcion'], precio = info['precio'], imagen = info['imagen'], stock = info['stock'])
            Producto.save()

            mensaje = "¡Producto agregado con éxito!"
            miFormulario = ProductosFormulario()
            return render(request, "AppFinal/productos.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = ProductosFormulario()
        return render(request, "AppFinal/productos.html", {"miFormulario":miFormulario})
     
def mensajes(request):
    if request.method == 'POST':
        miFormulario = MensajesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            pedido = Mensajes(nombre = info['nombre'], email = info['email'], comentario = info['comentario'])
            pedido.save()

            mensaje = "Su comentario ha sido añadido con éxito"
            miFormulario = MensajesFormulario()
            return render(request, "AppFinal/mensajes.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = MensajesFormulario()
        return render(request, "AppFinal/mensajes.html", {"miFormulario":miFormulario})

def eliminarMensaje(request, mensaje_nombre):
    mensaje = Mensajes.objects.get(nombre=mensaje_nombre)
    mensaje.delete()
 
    mensajes = Mensajes.objects.all()  # trae todos los mensajes
 
    contexto = {"mensajes": mensajes}
 
    return render(request, "AppFinal/leerMensajes.html", contexto)

def editarMensaje(request, mensaje_nombre):
    mensaje = Mensajes.objects.get(nombre=mensaje_nombre)

    if request.method == 'POST':

        miFormulario = MensajesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data

            mensaje.nombre = info['nombre']
            mensaje.email = info['email']
            mensaje.comentario = info['comentario']

            mensaje.save()

            mensajes = Mensajes.objects.all()
            context = {"mensajes":mensajes}
            return render(request, "AppFinal/leerMensajes.html", context) #mejor que te lleve a otra pagina como el inicio
    else:
        miFormulario = MensajesFormulario(initial={'nombre': mensaje.nombre, 'email': mensaje.email, 'comentario': mensaje.comentario})

    return render(request, "AppFinal/editarMensajes.html", {"miFormulario": miFormulario, "mensaje_nombre": mensaje_nombre})
