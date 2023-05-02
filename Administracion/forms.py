from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese un nombre"}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingrese un correo"}))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese un telefono"}))

class ProductosFormulario(forms.Form):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una descripcion del producto"}))
    codigo_producto = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese el codigo del producto. Ejemplo: 334588"}))

class PedidosFormulario(forms.Form):
    numero_pedido = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese el numero de pedido"}))
    ESTADOS_OPCIONES = [("pendiente", "pendiente"), ("entregado", "entregado")]
    estado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=ESTADOS_OPCIONES)
    notas = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una nota adicional"}), required=False)