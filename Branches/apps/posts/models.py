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
    comentario = TextField(max_length=255)
    fecha_creacion = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'comment_post')


    def __str__(self) -> str:
        return self.comentario
"""
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default= timezone.now, blank=True)
    es_borrador = models.BooleanField(default=False)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null= True)

    # foto = models.ImageField()

    class Meta:
        db_table = 'post'

    def __str__(self) -> str:

        return f"{self.id} {self.titulo}"
        """