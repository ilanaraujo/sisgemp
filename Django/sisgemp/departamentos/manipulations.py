# Manipulações no banco. Arquivo separado criado para aumentar a segurança

from .models import Departamento
from datetime import datetime
from funcionarios.models import Funcionario
from projetos.models import Projeto

# Cria um Departamento
def cria_novo_departamento(json_info):
    # Cria objeto com informações
    novo_departamento = Departamento(
        nome                = json_info['nome'],
        data_criacao        = datetime.now(),
        data_atualizacao    = datetime.now()
    )
    
    # Salva no banco, se possível
    try:
        novo_departamento.save()
    
    # Caso não seja possível salvar
    except:
        print("Erro ao criar o departamento")

# Recupera informações do departamento
def recupera_departamento(id_departamento):
    try:
        departamento = Departamento.objects.get(id=id_departamento)
        return departamento
    except:
        return None

# Lista todos os departamentos da Empresa
def lista_todos_departamentos():
    try:
        departamentos = Departamento.objects.all().order_by("id")
        return departamentos
    except:
        return None

# Lista todos os funcionários do departamento
def lista_funcionarios_departamento(id_departamento):
    try:
        funcionarios_departamento = Funcionario.objects.filter(departamento_id=id_departamento)
        return funcionarios_departamento
    except:
        return None

# Lista os projetos do departamento
def lista_projetos_departamento(id_departamento):
    try:
        projetos_departamento = Projeto.objects.filter(departamento_id=id_departamento)
        return projetos_departamento
    except:
        return None

# Atualiza informações do departamento
def edita_departamento(id_departamento, info):
    departamento = Departamento.objects.get(id=id_departamento)
    departamento.nome = info['nome']
    departamento.save()