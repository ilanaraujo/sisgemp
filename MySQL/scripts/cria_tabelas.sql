-- Cria o banco Empresa se o docker não tiver criado e o utiliza para as operações
CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

-- Cria as tabelas

-- Tabela com os sexos
CREATE TABLE IF NOT EXISTS tbl_sexos(
  id int AUTO_INCREMENT UNIQUE PRIMARY KEY,
  sexo varchar(9) UNIQUE,
  data_criacao datetime,
  data_atualizacao datetime
);

-- Tabela de Departamentos
CREATE TABLE IF NOT EXISTS tbl_departamentos(
  id int AUTO_INCREMENT UNIQUE PRIMARY KEY,
  nome varchar(50) UNIQUE,
  data_criacao datetime,
  data_atualizacao datetime
);

-- Tabela de Funcionários
CREATE TABLE IF NOT EXISTS tbl_funcionarios(
  id int AUTO_INCREMENT UNIQUE PRIMARY KEY,
  nome varchar(50) UNIQUE,
  cpf varchar(11) UNIQUE,
  rg varchar(9) UNIQUE,
  sexo_id int,
  nascimento datetime,
  possui_cnh boolean,
  salario float,
  departamento_id int,
  carga_horaria_semanal int,
  horas_livres int,
  data_criacao datetime,
  data_atualizacao datetime,
  FOREIGN KEY (sexo_id)
    REFERENCES tbl_sexos (id)
    ON DELETE CASCADE,
  FOREIGN KEY (departamento_id)
    REFERENCES tbl_departamentos (id)
    ON DELETE CASCADE
);

-- Tabela de Projetos
CREATE TABLE IF NOT EXISTS tbl_projetos (
  id int AUTO_INCREMENT UNIQUE PRIMARY KEY,
  departamento_id int,
  nome varchar(50) UNIQUE,
  horas_necessarias int,
  horas_realizadas int,
  prazo_estimado date,
  ultimo_calculo_hora date,
  supervisor_id int,
  horas_supervisao int,
  data_criacao datetime,
  data_atualizacao datetime,
  FOREIGN KEY (departamento_id)
    REFERENCES tbl_departamentos (id)
    ON DELETE CASCADE,
  FOREIGN KEY (supervisor_id)
    REFERENCES tbl_funcionarios (id)
    ON DELETE CASCADE
);

-- Tabela para relacionar funcionarios aos seus respectivos projetos
CREATE TABLE IF NOT EXISTS tbl_funcionarios_projetos (
  id int AUTO_INCREMENT UNIQUE PRIMARY KEY,
  funcionario_id int,
  projeto_id int,
  horas_trabalhadas int,
  data_criacao datetime,
  data_atualizacao datetime,
  FOREIGN KEY (funcionario_id)
    REFERENCES tbl_funcionarios (id)
    ON DELETE CASCADE,
  FOREIGN KEY (projeto_id)
    REFERENCES tbl_projetos (id)
    ON DELETE CASCADE
);

-- Insere as opções de sexo na tabela
INSERT INTO tbl_sexos (sexo, data_criacao, data_atualizacao) VALUES ('Feminino', now(), now());
INSERT INTO tbl_sexos (sexo, data_criacao, data_atualizacao) VALUES ('Masculino', now(), now());
INSERT INTO tbl_sexos (sexo, data_criacao, data_atualizacao) VALUES ('Outros', now(), now());