from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .manipulations import cadastra_funcionario, lista_projetos_funcionario, lista_todos_funcionarios, recupera_funcionario, edita_funcionario, lista_projetos_supervisionados_funcionario
from .forms import FormFuncionario
from .utils import extrai_dados_form_funcionario

# Exibe todos os funcionarios da empresa
def index(request):
    funcionarios = lista_todos_funcionarios()
    context = {
        'titulo' : 'Funcionários',
        'funcionarios' : funcionarios
    }
    return render(request, 'funcionarios/index.html', context)

# Cadastra um novo funcionario
def cadastro(request):
    if request.method == "POST":
        form = FormFuncionario(request.POST)
        
        if form.is_valid():
            infos = extrai_dados_form_funcionario(form)
            cadastra_funcionario(infos)
        return HttpResponseRedirect('/funcionarios')
    else:
        form = FormFuncionario()
        context = {
            'form':form,
            'titulo':'Cadastro de Funcionário'}
        return render(request, "funcionarios/form.html", context)

# Atualiza cadastro de um funcionário
def edita(request, id_funcionario):
    if request.method == "POST":
        form = FormFuncionario(request.POST)
        
        if form.is_valid():
            infos = extrai_dados_form_funcionario(form)
            edita_funcionario(id_funcionario, infos)
        
        return HttpResponseRedirect('/funcionarios')
    
    else:
        funcionario = recupera_funcionario(id_funcionario)
        
        informacoes = {
            'nome' : funcionario.nome,
            'cpf' : funcionario.cpf,
            'rg' : funcionario.rg,
            'sexo' : funcionario.sexo.id,
            'nascimento' : funcionario.nascimento,
            'possui_cnh' : funcionario.possui_cnh,
            'salario' : funcionario.salario,
            'departamento' : funcionario.departamento.id,
            'carga_horaria_semanal' : funcionario.carga_horaria_semanal
        }
        form = FormFuncionario(informacoes)
        context = {
            'form':form,
            'titulo':'Edita Funcionário'}
        return render(request, "funcionarios/form.html", context)

# Exibe os projetos nos quais o funcionario atua
def lista_projetos(request, id_funcionario):
    projetos = lista_projetos_funcionario(id_funcionario)
    projetos_supervisionados = lista_projetos_supervisionados_funcionario(id_funcionario)
    context = {
        'titulo' : 'Projetos do Funcionário',
        'projetos' : projetos,
        'projetos_supervisionados' : projetos_supervisionados
    }
    return render(request, 'funcionarios/projetos.html', context)
