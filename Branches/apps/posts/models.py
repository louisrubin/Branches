from django.db import models
from django.db.models.fields import CharField, DateTimeField, BooleanField

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    es_borrador = models.BooleanField()

    # foto = models.ImageField()

    class Meta:
        db_table = 'post'

    def __str__(self) -> str:

        return f"{self.id} {self.titulo}"