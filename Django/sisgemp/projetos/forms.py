from django import forms

class FormProjeto(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50, required=True)
    departamento = forms.IntegerField(label="Departamento", required=True)
    horas_necessarias = forms.IntegerField(label="Horas Necessárias", required=True)
    supervisor = forms.IntegerField(label="Supervisor", required=True)
    horas_supervisao = forms.IntegerField(label="Horas de Supervisão", required=True)

class FormInsereFuncionario(forms.Form):
    funcionario = forms.IntegerField(label="Funcionario", required=True)
    horas_trabalhadas = forms.IntegerField(label="Horas Dedicadas", required=True)

class FormRemoveFuncionario(forms.Form):
    funcionario = forms.IntegerField(label="Funcionario")