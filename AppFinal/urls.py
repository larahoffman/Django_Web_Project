from django.urls import path
from AppFinal import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about', views.about, name="About"),
    # path('leerProductos', views.leerProductos, name="LeerProductos"),
    path('productos/list', views.ProductosList.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', views.ProductosDetail.as_view(), name="Detail"),
    path(r'^nuevo$', views.ProductosCreate.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.ProductosUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductosDelete.as_view(), name="Delete"),
    # path('usuarios', views.usuarios, name="Usuarios"),
    # path('productos', views.productos, name="Productos"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('leerMensajes', views.leerMensajes, name="LeerMensajes"),
    path('eliminarMensaje/<mensaje_nombre>', views.eliminarMensaje, name="EliminarMensaje"),
    path('editarMensajes/<mensaje_nombre>', views.editarMensaje, name="EditarMensaje"),
    # path('pedidos', views.pedidos, name="Pedidos"),
    path('buscar', views.buscar, name="Buscar"),
    path('login', views.login_request, name="Login"),
    path('registro', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppFinal/index.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar")

]