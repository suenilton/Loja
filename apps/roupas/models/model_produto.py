from django.db import models
from django.urls import reverse
from datetime import datetime
from autoslug import AutoSlugField
from .model_categoria import Categoria


class Produto(models.Model):
    TAMANHO_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )
    nome_produto = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome_produto", default=None, null=True)
    preco_produto = models.CharField(max_length=20)
    marca_produto = models.CharField(max_length=100, blank=True)
    descricao_produto = models.CharField(max_length=200)
    tamanho_produto = models.CharField(max_length=1,choices=TAMANHO_CHOICES, blank=False, null=False)
    categoria_produto = models.ForeignKey(
        Categoria, related_name="produtos", on_delete=models.CASCADE
    )
    img_produto = models.ImageField(upload_to='fotos\%d\%m\%Y', blank=True)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    status_produto = models.BooleanField(verbose_name=('publicado'), default=False)

    def __str__(self) -> str:
        return self.nome_produto

    def get_absolute_url(self):
        return reverse('roupas:produtos_detalhados', kwargs={'slug': self.slug})
