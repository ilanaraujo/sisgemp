from django import forms
from funcionarios.utils import cria_lista_departamentos
from .utils import cria_lista_funcionarios

ESCOLHAS_DPTO = cria_lista_departamentos()
ESCOLHAS_FUNCIONARIOS = cria_lista_funcionarios()

class FormProjeto(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50, required=True)
    departamento = forms.IntegerField(label="Departamento", required=True, widget=forms.Select(choices=ESCOLHAS_DPTO))
    horas_necessarias = forms.IntegerField(label="Horas Necessárias", required=True)
    supervisor = forms.IntegerField(label="Supervisor", required=True, widget=forms.Select(choices=ESCOLHAS_FUNCIONARIOS))
    horas_supervisao = forms.IntegerField(label="Horas de Supervisão", required=True)

class FormInsereFuncionario(forms.Form):
    funcionario = forms.IntegerField(label="Funcionario", required=True, widget=forms.Select(choices=ESCOLHAS_FUNCIONARIOS))
    horas_trabalhadas = forms.IntegerField(label="Horas Dedicadas", required=True)

class FormRemoveFuncionario(forms.Form):
    funcionario = forms.IntegerField(label="Funcionario")
