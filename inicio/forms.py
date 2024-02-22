from django import forms


class CreacionUsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()