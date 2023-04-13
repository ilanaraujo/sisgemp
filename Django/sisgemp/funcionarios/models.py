from django.db import models
from departamentos.models import Departamento
from datetime import datetime

# Create your models here.

class Sexo(models.Model):
    id = models.IntegerField(primary_key=True)
    sexo = models.CharField(max_length=9, unique=True)
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.sexo

class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    nascimento = models.DateField()
    possui_cnh = models.BooleanField()
    salario = models.FloatField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    carga_horaria_semanal = models.IntegerField()
    horas_livres = models.IntegerField()
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.nome