# Biblioteca criada para funções auxiliares não serem executadas direto nas views
from departamentos.manipulations import lista_todos_departamentos


# Extrai informação do formulário de cadastro de funcionario
def extrai_dados_form_funcionario(formulario): 
    infos = {
    'nome' : formulario.cleaned_data["nome"],
    'cpf' : formulario.cleaned_data["cpf"],
    'rg' : formulario.cleaned_data["rg"],
    'sexo_id' : formulario.cleaned_data["sexo"],
    'nascimento' : formulario.cleaned_data["nascimento"],
    'possui_cnh' : formulario.cleaned_data["possui_cnh"],
    'salario' : formulario.cleaned_data["salario"],
    'departamento_id' : formulario.cleaned_data["departamento"],
    'carga_horaria_semanal' : formulario.cleaned_data["carga_horaria_semanal"]
    }
    return infos

def cria_lista_departamentos():
    departamentos = lista_todos_departamentos()
    lista_departamentos = list()
    for departamento in departamentos:
        item_lista = (
            departamento.id,
            departamento
        )
        lista_departamentos.append(item_lista)
    return lista_departamentos