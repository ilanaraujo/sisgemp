from django.db import models
from datetime import datetime

class Departamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nome