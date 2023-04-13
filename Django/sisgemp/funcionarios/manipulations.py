# Manipulações no banco. Arquivo separado criado para aumentar a segurança

from datetime import datetime
from .models import Funcionario, Sexo
from projetos.models import Projeto, FuncionarioProjeto
from departamentos.models import Departamento

def cadastra_funcionario(json_info):
    sexo_funcionario = Sexo.objects.get(id=json_info["sexo_id"])
    dpto_funcionario = Departamento.objects.get(id=json_info["departamento_id"])
    
    novo_funcionario = Funcionario(
        nome                    = json_info['nome'],
        cpf                     = json_info['cpf'],
        rg                      = json_info['rg'],
        sexo                 = sexo_funcionario,
        nascimento              = json_info['nascimento'],
        possui_cnh              = json_info['possui_cnh'],
        salario                 = json_info['salario'],
        departamento         = dpto_funcionario,
        carga_horaria_semanal   = json_info['carga_horaria_semanal'],
        horas_livres            = json_info['carga_horaria_semanal'],
        data_criacao            = datetime.now(),
        data_atualizacao        = datetime.now()
    )
    try:
        novo_funcionario.save()
    except:
        print("Não foi possível cadastrar o novo funcionario")

# Recupera um funcionário do banco
def recupera_funcionario(id_funcionario):
    try:
        funcionario = Funcionario.objects.get(id=id_funcionario)
        return funcionario
    except:
        return None

# Recupera todos os funcionarios
def lista_todos_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios

# Recupera projetos que o funcionario atua
def lista_projetos_funcionario(id_funcionario):
    try:
        id_projetos = FuncionarioProjeto.objects.filter(funcionario = id_funcionario)
        lista_projetos = list()
        for i in id_projetos:
            projeto = Projeto.objects.get(id=i.projeto_id)
            lista_projetos.append([projeto, i.horas_trabalhadas])
        return lista_projetos
    except:
        return None

# Lista projetos que o funcionario supervisiona
def lista_projetos_supervisionados_funcionario(id_funcionario):
    try:
        projetos_supervisionados = Projeto.objects.filter(supervisor = id_funcionario)
        return projetos_supervisionados
    except:
        return None

# Atualzia cadastro
def edita_funcionario(id_funcionario, json_info):
    horas_livres_anteriores = Funcionario.objects.get(id=id_funcionario).horas_livres
    diferenca_carga_horaria = json_info['carga_horaria_semanal'] - horas_livres_anteriores
    
    sexo_funcionario = Sexo.objects.get(id=json_info["sexo_id"])
    dpto_funcionario = Departamento.objects.get(id=json_info["departamento_id"])
    
    if (horas_livres_anteriores + diferenca_carga_horaria) >= 0:
        funcionario = Funcionario.objects.get(id=id_funcionario)
        funcionario.nome                    = json_info['nome']
        funcionario.cpf                     = json_info['cpf']
        funcionario.rg                      = json_info['rg']
        funcionario.sexo                    = sexo_funcionario
        funcionario.nascimento              = json_info['nascimento']
        funcionario.possui_cnh              = json_info['possui_cnh']
        funcionario.salario                 = json_info['salario']
        funcionario.departamento            = dpto_funcionario
        funcionario.carga_horaria_semanal   = json_info['carga_horaria_semanal']
        funcionario.horas_livres            = horas_livres_anteriores + diferenca_carga_horaria
        funcionario.data_atualizacao        = datetime.now()
        funcionario.save()
    else:
        print("Carga Horária menor do que a demanda de horas do funcionário")