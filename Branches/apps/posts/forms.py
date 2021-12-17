from django import forms
from django.db import models

from .models import Post

class Post_Form(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Post
        fields = ('cuerpo',
                'es_borrador',
                )
        labels = {
                'cuerpo':'Escribe aqui',
                'es_borrador':'Borrador',
        }

class Comment_Post():
        pass