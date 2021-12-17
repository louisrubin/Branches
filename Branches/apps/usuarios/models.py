from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField
import datetime as dt

# Create your models here.

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    writer = models.BooleanField(default=False)

    # foto = models.ImageField()

    class Meta:
        db_table = 'usuarios'

    def __str__(self) -> str:

        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "[ ... ]"

    
    