from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=100)

class Productos(models.Model):
    STOCK_OPCIONES = [("disponible", "disponible"), ("no disponible", "no disponible")]

    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.FileField(upload_to="productos")
    stock = models.CharField(max_length=50, choices=STOCK_OPCIONES) # hay o no stock disponible
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Nombre: {self.nombre} | Descripcion: {self.descripcion}"

class Mensajes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return f"Comentario: {self.comentario}"

# clase Perfil faltaria