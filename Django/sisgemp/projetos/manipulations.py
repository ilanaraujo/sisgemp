# Manipulações no banco. Arquivo separado criado para aumentar a segurança

from .models import Projeto, FuncionarioProjeto
from departamentos.models import Departamento
from funcionarios.models import Funcionario
from datetime import datetime, date, timedelta
from .utils import data_diferenca_dias

def cria_novo_projeto(informacoes):
    supervisor = Funcionario.objects.get(id=informacoes['supervisor'])
    departamento = Departamento.objects.get(id=informacoes['departamento'])
    if supervisor.horas_livres >= informacoes['horas_supervisao']:
        novo_projeto = Projeto(
            departamento = departamento,
            nome = informacoes['nome'],
            horas_necessarias = informacoes['horas_necessarias'],
            supervisor = supervisor,
            horas_supervisao = informacoes['horas_supervisao'],
            prazo_estimado = date(9999,12,31)
        )
        novo_projeto.save()
        supervisor.horas_livres -= informacoes['horas_supervisao']
        supervisor.save()
    else:
            print('Erro ao criar projeto')


def recupera_todos_projetos():
    projetos = Projeto.objects.all()
    return projetos

def insere_funcionario_projeto(id_projeto, informacoes):
    projeto = Projeto.objects.get(id=id_projeto)
    funcionario = Funcionario.objects.get(id=informacoes['funcionario'])    
    nova_insercao = FuncionarioProjeto(
        funcionario = funcionario,
        projeto = projeto,
        horas_trabalhadas = informacoes['horas_trabalhadas']
    )
    try:
        horas_livres_funcionario = funcionario.horas_livres
        if horas_livres_funcionario >= informacoes['horas_trabalhadas']:
            nova_insercao.save()
            novas_horas_livres = horas_livres_funcionario - informacoes['horas_trabalhadas']
            funcionario.horas_livres -= informacoes['horas_trabalhadas']
            funcionario.save()
    except:
        print('Erro ao inserir funcionário no projeto')

def remove_funcionario_projeto(id_projeto, id_funcionario):
    try:
        projeto_funcionario = FuncionarioProjeto.objects.filter(projeto = id_projeto).get(funcionario = id_funcionario)
        horas_dedicadas = projeto_funcionario.horas_trabalhadas
        projeto_funcionario.delete()
        funcionario = Funcionario.objects.get(id=id_funcionario)
        funcionario.horas_livres += horas_dedicadas
        funcionario.save()
    except:
        print("Erro ao retirar funcionário")

def altera_dados_projeto(id_projeto, informacoes):
    try:
        projeto = Projeto.objects.get(id=id_projeto)
        projeto.departamento = informacoes['departamento']
        projeto.nome = informacoes['nome']
        projeto.horas_necessarias = informacoes['horas_necessarias']
        projeto.supervisor = informacoes['supervisor']
        projeto.horas_supervisao = informacoes['horas_supervisao']
        projeto.data_atualizacao = datetime.now()
        projeto.save()
    except:
        print("Erro ao editar dados")

# Estima o prazo
def calcula_prazo_projeto(id_projeto):
    try:
        funcionarios_projeto = FuncionarioProjeto.objects.filter(projeto = id_projeto)
        projeto = Projeto.objects.get(id=id_projeto)
        total_horas_dedicadas = 0
        for funcionario in funcionarios_projeto:
            total_horas_dedicadas += funcionario.horas_trabalhadas
        if total_horas_dedicadas > 0:
            ultimo_calculo = projeto.ultimo_calculo_horas
            horas_realizadas = projeto.horas_realizadas
            dias_desde_ultimo_calculo = data_diferenca_dias(date.today().strftime("%Y-%m-%d"), ultimo_calculo.strftime("%Y-%m-%d"))
            semanas_completas_desde_ultimo_calculo = dias_desde_ultimo_calculo // 7
            horas_realizadas_desde_ultimo_calculo = horas_realizadas * semanas_completas_desde_ultimo_calculo
            horas_realizadas += horas_realizadas_desde_ultimo_calculo
            horas_restantes = projeto.horas_necessarias - horas_realizadas
            semanas_restantes = horas_restantes // total_horas_dedicadas
            dias_restantes = semanas_restantes * 7
            novo_prazo = date.today() + timedelta(days=dias_restantes)
            projeto.prazo_estimado = novo_prazo
            projeto.data_atualizacao = datetime.now()
            projeto.save()
        else:
            projeto.prazo_estimado = date(9999, 12, 31)
            projeto.save()
    except:
        print("Erro ao calcular prazo")

# Exibe funcionários daquele projeto
def recupera_funcionarios_projeto(id_projeto):
    funcionarios = FuncionarioProjeto.objects.filter(projeto=id_projeto)
    return funcionarios    

# Recupera um projeto do banco
def recupera_projeto(id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return projeto