from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} | Correo: {self.correo} | Telefono: {self.telefono}"

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    codigo_producto = models.IntegerField()

    def __str__(self):
        return f"Descripcion: {self.descripcion} | Codigo de producto: {self.codigo_producto}"

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    numero_pedido = models.IntegerField()
    ESTADOS_OPCIONES = [("pendiente", "pendiente"), ("entregado", "entregado")]
    estado = models.CharField(max_length=15, choices=ESTADOS_OPCIONES, default="pendiente")
    notas = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"Nro pedido: {self.numero_pedido} | Estado: {self.estado} | Notas: {self.notas}"