from django import forms

class FormDepartamento(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50, required=True)
