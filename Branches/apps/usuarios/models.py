from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

from django.contrib.auth.models import AbstractUser

def calcular_edad(fecha):
    pass

class Usuario(AbstractUser):
    fecha_nacimiento = models.DateTimeField(null=True)

    # foto = models.ImageField()

    class Meta:
        db_table = 'usuarios'

    def __str__(self) -> str:

        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "[ ... ]"

