from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("novo/", views.novo, name="novo_departamento"),
    path("<int:id_departamento>/projetos/", views.lista_projetos, name="lista_projetos"),
    path("<int:id_departamento>/funcionarios/", views.lista_funcionarios, name="lista_funcionarios"),
    path("<int:id_departamento>/editar", views.edita, name="edita_departamento")
]