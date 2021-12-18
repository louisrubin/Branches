from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    #nombre = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Usuario
        fields = ["username", 
                "first_name",
                'last_name',
                'email',
                'comment',
                'writer',
                'es_administrador',
                'is_superuser',
                ]
        labels = {"username": "Nombre de Usuario", 
                "first_name": "Nombre", 
                'last_name': 'Apellido',
                'email': 'Correo',
                'comment': 'Comentar',
                'writer': 'Escritor',
                'es_administrador': 'Administrador',
                'is_superuser': 'Super User',
                }
        

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            }