# Biblioteca criada para funções auxiliares não serem executadas direto nas views

from datetime import datetime

# Extrai os dados do formulário de criação de projeto
def extrai_dados_form_projeto(form):
    informacoes = {
        'nome' : form.cleaned_data['nome'],
        'departamento' : form.cleaned_data['departamento'],
        'horas_necessarias' : form.cleaned_data['horas_necessarias'],
        'supervisor' : form.cleaned_data['supervisor'],
        'horas_supervisao' : form.cleaned_data['horas_supervisao']
    }
    return informacoes

# Retorna, em dias, a diferença absoluta de duas datas
def data_diferenca_dias(data1, data2):
    data1 = datetime.strptime(data1, "%Y-%m-%d")
    data2 = datetime.strptime(data2, "%Y-%m-%d")
    return abs((data2 - data1).days)