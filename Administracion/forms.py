from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()