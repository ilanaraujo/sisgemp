from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .manipulations import edita_departamento, cria_novo_departamento, recupera_departamento, lista_todos_departamentos, lista_funcionarios_departamento, lista_projetos_departamento
from .forms import FormDepartamento

# Lista todos os departamentos da empresa
def index(request):
    todos_departamentos = lista_todos_departamentos()
    context = {'departamentos' : todos_departamentos, 'titulo':'Departamentos'}
    return render(request, "departamentos/index.html", context)

# Cria um novo departamento
def novo(request):
    if request.method == "POST":
        form = FormDepartamento(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            infos = {'nome' : nome}
            cria_novo_departamento(infos)
        return HttpResponseRedirect('/departamentos')
    else:
        form = FormDepartamento()
        context = {
            'form':form,
            'titulo':'Novo Departamento'}
        return render(request, "departamentos/form.html", context)

def lista_projetos(request, id_departamento):
    departamento = recupera_departamento(id_departamento)
    projetos = lista_projetos_departamento(id_departamento)
    context = {
        'titulo' : 'Projetos no Departamento',
        'departamento' : departamento,
        'projetos' : projetos
    }
    
    return render(request, 'departamentos/projetos.html', context)

def lista_funcionarios(request, id_departamento):
    departamento = recupera_departamento(id_departamento)
    funcionarios = lista_funcionarios_departamento(id_departamento)
    context = {
        'titulo' : 'Funcionários do Departamento',
        'departamento' : departamento,
        'funcionarios' : funcionarios
    }
    return render(request, 'departamentos/funcionarios.html', context)

def edita(request, id_departamento):
    if request.method == "POST":
        form = FormDepartamento(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            infos = {'nome' : nome}
            edita_departamento(id_departamento, infos)
        return HttpResponseRedirect('/departamentos')
    else:
        departamento = recupera_departamento(id_departamento)
        
        dict_dpto = {'nome':departamento.nome}
        form = FormDepartamento(dict_dpto)
        context = {
            'form':form,
            'titulo':'Novo Departamento'}
        return render(request, "departamentos/form.html", context)
    