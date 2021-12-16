from django.db import models
from django.db.models.fields import CharField, DateTimeField, BooleanField
from django.db.models.fields.related import ForeignKey
#from datetime import datetime  

from apps.usuarios.models import Usuario

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    es_borrador = models.BooleanField(default=False)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null= True)

    # foto = models.ImageField()

    class Meta:
        db_table = 'post'

    def __str__(self) -> str:

        return f"{self.id} {self.titulo}"