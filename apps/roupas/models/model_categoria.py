from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.urls import reverse


class Categoria(TimeStampedModel):
    nome_categoria = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome_categoria")

    class Meta:
        ordering = ("nome_categoria",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome_categoria
    
    def get_absolute_url(self):
        return reverse("roupas:produtos_por_categoria", kwargs={'slug': self.slug})
