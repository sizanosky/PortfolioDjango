from datetime import datetime
from django.db import models

# Create your models here.


class Projeto(models.Model):
    """
    Classe para modelar e criar banco de dados de projetos para um APP
    """
    nome_projeto = models.CharField(max_length=200)
    descricao_projeto = models.TextField()
    cliente = models.CharField(max_length=100)
    data_conclusao = models.DateTimeField(default=datetime.now, blank=True)
    website = models.CharField(max_length=200)
    linguagem = models.CharField(max_length=100)
    tags_projeto = models.TextField()
    detahes_projeto = models.TextField()
