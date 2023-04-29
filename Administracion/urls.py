from django.urls import path
from Administracion import views

urlpatterns = [
    path('', views.inicio),
    path('clientes', views.clientes, name="Clientes"),
    path('productos', views.productos),
    path('pedidos', views.pedidos)
]