from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.cadastro, name="novo"),
    path("<int:id_funcionario>/editar", views.edita, name="edita"),
    path("<int:id_funcionario>/projetos", views.lista_projetos, name="lista_projetos")
]