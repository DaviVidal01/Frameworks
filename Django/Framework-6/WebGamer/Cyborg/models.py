from django.db import models
from datetime import datetime
# Create your models here.

class Teste(models.Model):
    nome_card = models.CharField(max_length = 200)
    description = models.TextField()
    path = models.TextField()
    primeiro_texto = models.TextField()
    segundo_texto = models.TextField()
    alunos = models.IntegerField()
    date_create = models.DateTimeField(default = datetime.now, blank = True)

class NovaTabela(models.Model):
    titulo = models.CharField(max_length = 255)
    descricao = models.TextField()
    imagem = models.ImageField()
    pontos = models.DecimalField(max_digits=4, decimal_places=1 )