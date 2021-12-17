from django.db import models
from django.db.models.fields import CharField, DateTimeField, BooleanField, TextField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

from apps.usuarios.models import Usuario


class Post(models.Model):
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'autor_post', null=True)
    likes = models.ManyToManyField(Usuario, blank= True, related_name= 'likes')
    es_borrador = models.BooleanField(default=False)

class Comentario(models.Model):
    comentario = TextField()
    fecha_creacion = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= 'comment_post')
    likes = models.ManyToManyField(Usuario, blank= True, related_name= 'comment_likes')


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