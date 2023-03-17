from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date


# Create your models here.
class Usuario(AbstractUser,models.Model):    
    # escritorioId = models.ForeignKey(Escritorio, db_column='escritorio_id', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'tb_user'
        pass

