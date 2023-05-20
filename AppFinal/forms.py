from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppFinal.models import Productos, Mensajes

STOCK_OPCIONES = [("disponible", "disponible"), ("no disponible", "no disponible")]
CATEGORIAS = [("Sillas de oficina", "Sillas de oficina"), ("Escritorios", "Escritorios")]

class ProductosFormulario(forms.Form):

    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(attrs={"cols": 80, "rows": 20, "class": "form-control"}),
            "imagen": forms.ImageField(widget=forms.ImageField)
            #falta completar (idem para Mensajes)
        }

class MensajesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su nombre"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su correo"}))
    comentario = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Mensajes
        fields = '__all__'
    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su nombre"}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido", required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField(label="Apellido", required=False)
    first_name = forms.CharField(label="Nombre", required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)