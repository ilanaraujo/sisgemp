# Biblioteca criada para funções auxiliares não serem executadas direto nas views

from datetime import datetime
from funcionarios.manipulations import lista_todos_funcionarios

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

def cria_lista_funcionarios():
    funcionarios = lista_todos_funcionarios()
    lista_funcionarios = list()
    for funcionario in funcionarios:
        item_lista = (
            funcionario.id,
            funcionario
        )
        lista_funcionarios.append(item_lista)
    return lista_funcionarios