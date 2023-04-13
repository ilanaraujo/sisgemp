from django.db import models
from datetime import datetime, date
from departamentos.models import Departamento
from funcionarios.models import Funcionario

class Projeto(models.Model):
    id = models.IntegerField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True)
    horas_necessarias = models.IntegerField()
    horas_realizadas = models.IntegerField(default=0)
    prazo_estimado = models.DateField(default=date(9999,12,31))
    ultimo_calculo_horas = models.DateField(default=datetime.now())
    supervisor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    horas_supervisao = models.IntegerField()
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())

class FuncionarioProjeto(models.Model):
    id = models.IntegerField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    horas_trabalhadas = models.IntegerField()
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())