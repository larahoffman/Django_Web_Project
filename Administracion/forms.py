from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

class ProductosFormulario(forms.Form):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    codigo_producto = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

class PedidosFormulario(forms.Form):
    numero_pedido = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    ESTADOS_OPCIONES = [("pendiente", "pendiente"), ("entregado", "entregado")]
    estado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=ESTADOS_OPCIONES)
    notas = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)