# SIstema em MySQL

## Introdução

Esse sistema foi feito utilizando MySQL. Foram criadas Stored Procedures que realizam o CRUD a partir de um JSON que recebem. Criei duas Procedures para cada ação: uma que recebe um JSON, extrai seus dados e chama segunda, que, a partir dos dados recebidos, executa a ação correspondente. Essa decisão foi tomada para ter um controle maior sobre as Procedures durante testes realizados.

## Ferramentas utilizadas
- MySQL, versão 5.7
- Docker, versão 23.0.2
- Docker Compose, versão 1.25
- DataGrip, versão 2023.1
  - Utilizado para acesso ao banco.
 
## Requisitos
Antes de iniciar o sistema, os seguintes passos devem ser seguidos:
  - Instalação do Docker, cujo tutorial está presente em seu site oficial.
  - Instalação do Docker Compose, através do comando `$ sudo apt install docker-compose`
 
## Inicialização
Estando nesta pasta (`/sisgemp/MySQL/`), rode o seguinte comando no terminal:
`$ sudo docker compose up -d`

Para confirmar que o contêinar estã em execução, execute
`$ sudo docker ps`

Após confirmar que o contêiner está online, execute os scripts na pasta `/MySQL/scripts/`, seguindo a ordem:
- `cria_tabelas.sql`: Cria o banco `empresa` e cinco tabelas: `tbl_departamentos`, `tbl_sexos`, `tbl_funcionarios`, `tbl_projetos`, `tbl_funcionarios_projetos`. Elas representam, respectivamente:
  - Os departamentos da empresa;
  - Os sexos que os funcionários podem ter. 
    - OBS: Preferi criar essa tabela a parte de forma a economizar espaço no banco, pois utilizar um INT (Chave Estrangeira) ocupa menos espaço que um VARCHAR de 10 dígitos. O script também a preenche automaticamente;
  - Os funcionários da empresa;
  - Os projetos da empresa;
  - Um mapeamento de qual(is) funcionário(s) estão em qual(is) projeto(s);

- `cria_procedures.sql`: Cria as Procedures que serão utilizadas para realizar o CRUD. São elas:
  - `usp_Insere_Departamento`: Cria um departamento
  - `usp_Insere_Funcionario`: Cria um funcionário
  - `usp_Aumenta_Carga_horaria`: Cria um projeto
  - `usp_Reduz_Carga_Horaria`: Aumenta a carga horária semanal de um funcionário
  - `usp_Aumenta_Horas_Livres`: Diminui a carga horária semanal de um funcionário
  - `usp_Reduz_Horas_Livres`: Aumenta as horas disponíveis de um funcionário
  - `usp_Insere_Projeto`: Reduz as horas disponíveis do funcionário
  - `usp_Troca_Supervisor_Projeto`: Altera o supervisor de um projeto
  - `usp_Insere_Funcionario_Projeto`: Aloca um funcionário em um projeto
  - `usp_Retira_Funcionario_Projeto`: Retira um funcionário do projeto
  - `usp_Calcula_Prazo_Estimado`: Estima o prazod e conclusão do projeto

- `cria_procedures_json.sql`: Cria procedures relacionadas às criadas anteriormente. Estas recebem um JSON, extraem seus dados e chamam a procedure correspondente.

Pronto, o sistema está completo. Foram criados scripts de Testes, disponíveis [aqui](https://github.com/ilanaraujo/sisgemp/tree/main/MySQL/scripts/testes)
  
