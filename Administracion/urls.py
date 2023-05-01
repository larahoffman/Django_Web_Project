from django.urls import path
from Administracion import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name="Clientes"),
    path('productos', views.productos, name="Productos"),
    path('pedidos', views.pedidos, name="Pedidos"),
    path('buscar', views.buscar)
]