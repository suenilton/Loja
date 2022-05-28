from tkinter import CASCADE
from typing import cast
from django.db import models
from datetime import datetime
from . import Produto


class ConjuntoRoupas(models.Model):
    NUMERO_CHOICES = (
        ('1', 'imagem 01'),
        ('2', 'imagem 02'),
        ('3', 'imagem 03'),
        ('4', 'imagem 04'),
    )

    numero_conjunto = models.CharField(max_length=1, choices=NUMERO_CHOICES, blank=False, null=False, default=None)
    nome_conjunto = models.CharField(max_length=200)
    nome_produtos_do_conjunto = models.ManyToManyField(Produto, related_name='conjuntos')
    preco_conjunto = models.CharField(max_length=20)
    descricao_conjunto = models.CharField(max_length=200)
    categoria_conjunto = models.CharField(max_length=100)
    img_conjunto = models.ImageField(upload_to='fotos\%d\%m\%Y', blank=True)
    data_conjunto = models.DateTimeField(default=datetime.now, blank=True)
    status_conjunto = models.BooleanField(verbose_name=('publicado'), default=False)

    def __str__(self) -> str:
        return self.nome_conjunto