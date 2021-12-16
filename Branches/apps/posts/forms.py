from django import forms
from django.db import models

from .models import Post

class PostForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Post
        fields = ('titulo',
                'descripcion',
                'es_borrador',
                'usuario',
                )
        labels = {
                'titulo':'Titulo',
                'descripcion':'Descripcion',
                'es_borrador':'Borrador',
        }
