from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("novo/", views.novo_projeto, name="novo"),
    path("<int:id_projeto>/insere_funcionario/", views.insere_funcionario, name="insere_funcionario"),
    path("<int:id_projeto>/remove_funcionario/", views.remove_funcionario, name="remove_funcionario"),
    path("<int:id_projeto>/editar", views.altera_dados, name="altera_dados"),
    path("<int:id_projeto>/calcula_prazo", views.calcula_prazo, name="calcula_prazo"),
    path("<int:id_projeto>", views.detalhes_projeto, name="detalhes_projeto")
]