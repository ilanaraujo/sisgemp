# Sistema em Django

## Introdução
Esse sistema foi desenvolvido em Django e até o prazo final não foi possível executá-lo em um contêiner. 

## Ferramentas Utilizadas
- Django, versão 4.2
- Python, versão 3.8
- Pip, versão 20.0.2

## Requisitos
Para rodar o sistema, antes instale o `django` com o comando:
`$ pip install django==4.2`

## Inicialização
Para iniciar o sistema, vá para a pasta `/Django/sisgemp/` e execute `$ python3 manage.py runserver 0.0.0.0:8000`. Dessa forma, o sistema estará acessível no endereço localhost:8000.

## Uso

O sistema possui as aplicações departamentos, funcionarios e projetos. Elas possuem as sequintes páginas:

Departamentos:
  - /departamentos: Lista todos os departamentos
  - /departamentos/novo: Cria um departamento
  - /departamentos/(id)/projetos: Lista os projetos do departamento com id correspondente
  - /departamentos/(id)/funcionarios: Lista os funcionarios do departamento com id correspondente
  - /departamentos/(id)/editar: Atualiza os dados do departamento com id correspondente

Funcionários:
  - /funcionarios: Lista todos os funcionarios
  - /funcionarios/cadastro: Cadastra um novo funcionário
  - /funcionarios/<id>/editar: Atualiza o cadastro do funcionário com aquele id
  - /funcionarios/<id>/projetos: Exibe projetos que funcionário com aquele id trabalha

Projetos:
  - /projetos: Lista todos os projetos
  - /projetos/novo: Cria projeto
  - /projetos/<id>/insere_funcionario: Coloca um funcionário em um projeto
  - /projetos/<id>/remove_funcionario: Retira funcionário do projeto
  - /projetos/<id>/editar: Atualiza os dados do projeto
  - /projetos/<id>/calcular_prazo: Estima o prado do projeto
  - /projetos/<id>: Exibe funcionários que trabalham no projeto

As tabelas do banco são semelhantes às do sistema em MySQL.

Na pasta de cada aplicação existe um arquivo `manipulations.py`, responsável por fazer as manipulações no banco. Usá-lo ao invés de fazer nas views torna o sistema menos vulnerável. Além disso, támbém tem o arquivo `utils.py`, responsável por guardar funções auxiliares. Colocá-las no arquivo de manipulação ou de views deixaria o código mais desorganizado.

Testes foram executados localmente, e o sistema teve o comportamento esperado.
