from dataclasses import dataclass
from django.db import models

# Create your models here.

class Dolar (models.Model):
    data = models.DateField()
    slug = models.SlugField()
    hora = models.models.IntegerField()
    preco = models.FloatField(max_length=4)
    