from django.db import models
from datetime import datetime


class Produto(models.Model):
    TAMANHO_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )
    nome_produto = models.CharField(max_length=200)
    preco_produto = models.CharField(max_length=20)
    marca_produto = models.CharField(max_length=100, blank=True)
    descricao_produto = models.CharField(max_length=200)
    tamanho_produto = models.CharField(max_length=1,choices=TAMANHO_CHOICES, blank=False, null=False)
    categoria_produto = models.CharField(max_length=100)
    img_produto = models.ImageField(upload_to='fotos\%d\%m\%Y', blank=True)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    status_produto = models.BooleanField(verbose_name=('publicado'), default=False)

    def __str__(self) -> str:
        return self.nome_produto
