from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('leerProductos', views.leerProductos, name="LeerProductos"),
    # path('usuarios', views.usuarios, name="Usuarios"),
    path('productos', views.productos, name="Productos"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('leerMensajes', views.leerMensajes, name="LeerMensajes"),
    path('eliminarMensaje/<mensaje_nombre>', views.eliminarMensaje, name="EliminarMensaje"),
    path('editarMensajes/<mensaje_nombre>', views.editarMensaje, name="EditarMensaje")
    # path('pedidos', views.pedidos, name="Pedidos"),
    # path('buscar', views.buscar, name="Buscar")
]