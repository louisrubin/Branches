from django.db import models
from django.db.models.fields import CharField, DateTimeField, BooleanField, TextField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

from apps.usuarios.models import Usuario


class Post(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'autor_post', null=True)
    es_borrador = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return self.cuerpo


class Comentario(models.Model):
    comentario = models.TextField(max_length=255)
    fecha_creacion = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'comment_post')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.comentario

        