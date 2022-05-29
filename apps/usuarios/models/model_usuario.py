from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    campoextra = models.CharField(max_length=200, blank=True)

class Usuario1(models.Model):

    nome_usuario = models.CharField(max_length=200)
    email_usuario = models.EmailField(max_length=200)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=300)
    bairro = models.CharField(max_length=50)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    senha_usuario = models.CharField(max_length=200)
    confirmacao_senha_usuario = models.CharField(max_length=200)
