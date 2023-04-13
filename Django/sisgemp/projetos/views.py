from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .manipulations import recupera_todos_projetos, insere_funcionario_projeto, remove_funcionario_projeto, cria_novo_projeto, altera_dados_projeto, calcula_prazo_projeto, recupera_funcionarios_projeto, recupera_projeto
from .forms import FormProjeto, FormInsereFuncionario, FormRemoveFuncionario
from .utils import extrai_dados_form_projeto

# Lista todos os Projetos
def index(request):
    projetos = recupera_todos_projetos()
    context = {
        'titulo' : 'Projetos',
        'projetos' : projetos
    }
    return render(request, 'projetos/index.html', context)

# Cria um novo Projeto
def novo_projeto(request):
    if request.method == "POST":
        form = FormProjeto(request.POST)
        
        if form.is_valid():
            infos = extrai_dados_form_projeto(form)
            cria_novo_projeto(infos)
        return HttpResponseRedirect('/projetos')
    else:
        form = FormProjeto()
        context = {
            'titulo' : 'Criar novo projeto',
            'form' : form
        }
        return render(request, 'projetos/form.html', context)

# Insere um funcionário em um projeto
def insere_funcionario(request, id_projeto):
    if request.method == 'POST':
        form = FormInsereFuncionario(request.POST)
        
        if form.is_valid():
            infos = {
                'funcionario' : form.cleaned_data['funcionario'],
                'horas_trabalhadas' : form.cleaned_data['horas_trabalhadas']
            }
            insere_funcionario_projeto(id_projeto, infos)
        return HttpResponseRedirect('/projetos')
    else:
        form = FormInsereFuncionario()
        context = {
            'titulo' : 'Insere Funcionário',
            'form' : form
        }
        return render(request, 'projetos/form.html', context)

# Remove um funcionário de um projeto
def remove_funcionario(request, id_projeto):
    if request.method == 'POST':
        form = FormRemoveFuncionario(request.POST)
        if form.is_valid():
            funcionario = form.cleaned_data['funcionario']
            remove_funcionario_projeto(id_projeto, funcionario)
        return HttpResponseRedirect('/projetos')
    else:
        form = FormRemoveFuncionario()
        context = {
            'titulo' : 'Remove Funcionário',
            'form' : form
        }
        return render(request, 'projetos/form.html', context)

def altera_dados(request, id_projeto):
    if request.method == 'POST':
        form = FormProjeto(request.POST)
        
        if form.is_valid():
            infos = extrai_dados_form_projeto(form)
            altera_dados_projeto(id_projeto, infos)
        return HttpResponseRedirect('/projetos')
    else:
        form = FormProjeto()
        context = {
            'titulo' : 'Altera Dados',
            'form' : form
        }
        return render(request, 'projetos/form.html', context)

def calcula_prazo(request, id_projeto):
    calcula_prazo_projeto(id_projeto)
    return HttpResponseRedirect('/projetos')

def detalhes_projeto(request, id_projeto):
    funcionarios = recupera_funcionarios_projeto(id_projeto)
    context = {
        'titulo' : 'Detalhes do projeto',
        'funcionarios' : funcionarios,
        'projeto' : recupera_projeto(id_projeto)
    }
    return render(request, 'projetos/detalhes.html', context)