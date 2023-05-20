from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    # avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppFinal/index.html')

def about(request):
    return render(request, "AppFinal/about.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Productos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFinal/index.html", {"productos":productos, "nombre":nombre})
    else:
        respuesta = "Ingrese un nombre"
        return render(request, "AppFinal/index.html", {"respuesta":respuesta})

# def leerProductos(request):
#     productos = Productos.objects.all()
#     context = {"productos":productos}
#     return render(request, "AppFinal/leerProductos.html", context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppFinal/index.html")
            else:
                mensajeError = "Error, datos incorrectos"
                return render(request, "AppFinal/login.html", {"mensajeError": mensajeError})
        else:
            mensajeForm = "Usuario o contraseña incorrectos"
            form = AuthenticationForm() #limpio los datos
            return render(request, "AppFinal/login.html", {"form":form, "mensajeForm": mensajeForm})
    
    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            form = UserRegisterForm()
            mensaje = "Usuario creado con éxito"
            return render(request, "AppFinal/registro.html", {"form": form, "mensaje":mensaje})
        else:
            mensajeError = "Error al generar el usuario"
            return render(request, "AppFinal/registro.html", {"form": form, "mensaje":mensajeError})
    else:
        form = UserRegisterForm()

    return render(request, "AppFinal/registro.html", {"form": form})

class ProductosList(ListView):
    model = Productos
    context_object_name = "productos"
    template_name = "AppFinal/productos_list.html"

class ProductosDetail(DetailView):
    model = Productos
    template_name = "AppFinal/productos_detalle.html"

class ProductosCreate(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = "AppFinal/productos_create.html"
    success_url = "/productos/list"
    fields = '__all__'

class ProductosUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    success_url = "/productos/list"
    fields = '__all__'

class ProductosDelete(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = "/productos/list"

def leerMensajes(request):
    mensajes = Mensajes.objects.all()
    context = {"mensajes":mensajes}
    return render(request, "AppFinal/leerMensajes.html", context)

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

@login_required
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

@login_required
def eliminarMensaje(request, mensaje_nombre):
    mensaje = Mensajes.objects.get(nombre=mensaje_nombre)
    mensaje.delete()
 
    mensajes = Mensajes.objects.all()  # trae todos los mensajes
 
    contexto = {"mensajes": mensajes}
 
    return render(request, "AppFinal/leerMensajes.html", contexto)

@login_required
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

@login_required
def editarPerfil(request):
    
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppFinal/index.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def avatar(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'layout.html', {'user_avatar': user_avatar})

from django.contrib.auth.models import User
from .forms import AvatarFormulario
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
        if miFormulario.is_valid():   #Si pasó la validación de Django
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
            avatar.save()
            return render(request, "AppFinal/index.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "AppFinal/agregarAvatar.html", {"miFormulario":miFormulario})