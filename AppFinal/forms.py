from django import forms

class ProductosFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre del producto"}))
    categoria = forms.InlineForeignKeyField(widget=forms.Select(attrs={"class": "form-select"})) #creo que acabo de inventar algo
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una descripcion del producto"}))
    # codigo_producto = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese el codigo del producto. Ejemplo: 334588"}))

#class MensajesFormulario(forms.Form):
    # numero_pedido = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese el numero de pedido"}))
    # ESTADOS_OPCIONES = [("pendiente", "pendiente"), ("entregado", "entregado")]
    # estado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=ESTADOS_OPCIONES)
    # notas = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una nota adicional"}), required=False)