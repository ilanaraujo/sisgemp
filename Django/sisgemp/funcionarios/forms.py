from django import forms
from .utils import cria_lista_departamentos

ESCOLHAS_SEXO = [
    (1, 'Feminino'),
    (2, 'Masculino'),
    (3, 'Outros')
]

ESCOLHAS_CNH = [
    (False, 'Não'),
    (True, 'Sim')
]

ESCOLHAS_DPTO = cria_lista_departamentos()

class FormFuncionario(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50, required=True)
    cpf = forms.CharField(label="CPF", max_length=11, required=True)
    rg = forms.CharField(label="RG", max_length=9, required=True)
    sexo = forms.IntegerField(label="Sexo", widget=forms.Select(choices=ESCOLHAS_SEXO))
    nascimento = forms.DateField(label="Nascimento", required=True)
    possui_cnh = forms.BooleanField(label="Possui CNH", widget=forms.Select(choices=ESCOLHAS_CNH), required=False)
    salario = forms.FloatField(label="Salário", required=True)
    departamento = forms.IntegerField(label="Departamento", required=True, widget=forms.Select(choices=ESCOLHAS_DPTO))
    carga_horaria_semanal = forms.IntegerField(label="Carga Horária Semanal", required=True)

