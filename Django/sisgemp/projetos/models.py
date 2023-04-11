from django.db import models
from datetime import datetime
from sisgemp.departamentos.models import Departamento
from sisgemp.funcionarios.models import Funcionario

# Create your models here.

class Projeto(models.Model):
    id = models.IntegerField(primary_key=True)
    departamento_id = models.ForeignKey(Departamento, db_column=id, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    horas_necessarias = models.IntegerField()
    horas_realizadas = models.IntegerField(default=0)
    prazo_estimado = models.DateField(default=None)
    ultimo_calculo_horas = models.DateTimeField(default=datetime.now())
    supervisor_id = models.ForeignKey(Funcionario, db_column='id', on_delete=models.CASCADE)
    horas_supervisao = models.IntegerField()
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())

class FuncionarioProjeto(models.Model):
    id = models.IntegerField(primary_key=True)
    funcionario_id = models.ForeignKey(Funcionario, db_column='id', on_delete=models.CASCADE)
    projeto_id = models.ForeignKey(Projeto, db_column='id', on_delete=CASCADE)
    horas_trabalhadas = models.IntegerField()
    data_criacao = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())