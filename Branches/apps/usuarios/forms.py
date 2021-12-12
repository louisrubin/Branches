from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from .models import Usuario

class ProductoForm(forms.ModelForm):
    #nombre = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Usuario
        fields = ["username", 
                "first_name",
                'last_name',
                'email',
                'is_superuser',
                ]
        labels = {"username": "Nombre de Usuario", 
                "first_name": "Nombre", 
                'last_name': 'Apellido',
                'email': 'Correo',
                'is_superuser': 'Admin',
                }


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            }