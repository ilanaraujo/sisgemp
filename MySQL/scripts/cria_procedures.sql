-- CREATE PROCEDURE novo_projeto (
--     IN nome_projeto VARCHAR(50),
--     IN nome_departamento VARCHAR(50))
-- BEGIN
--     IF NOT SELECT nome FROM tb_projeto WHERE nome = nome_projeto
--     BEGIN
--         INSERT INTO tb_projeto (nome, )

CREATE PROCEDURE usp_Insere_Departamento(IN nome_dpto VARCHAR(50))
    BEGIN
        INSERT INTO tbl_departamentos (nome, data_criacao, data_atualizacao)
            VALUES (nome_dpto, now(), now());
    END;

CREATE PROCEDURE usp_Insere_Sexo(IN novo_sexo VARCHAR(9))
    BEGIN
    INSERT INTO tbl_sexos (sexo, data_criacao, data_atualizacao)
    VALUES (novo_sexo, now(), now());
    END;

CREATE PROCEDURE usp_Insere_Projeto(IN id_departamento INT, IN novo_projeto VARCHAR (50), IN horas INT, IN prazo INT, IN supervisor INT, IN horas_supervisor INT)
BEGIN
    DECLARE @horas_livres_supervisor INT;
    SET @horas_livres_supervisor := (SELECT MAX(horas_livres) FROM tbl_funcionarios WHERE id = supervisor);
    IF NOT (horas_livres_supervisor < horas_supervisor) THEN
        INSERT INTO tbl_projetos (departamento_id, nome, horas_para_conclusao, prazo_estimado, horas_realizadas, dt_ultimo_calculo_hora, supervisor_id, data_criacao, data_atualizacao)
        VALUES (id_departamento, novo_projeto, horas, null, 0, CURDATE(), supervisor, now(), now());
        id_projeto_novo = SELECT id FROM tbl_projetos WHERE nome = novo_projeto;
        INSERT INTO tbl_funcionarios_projetos (funcionario_id, projeto_id, horas_trabalhadas, data_criacao, data_atualizacao)
        VALUES (supervisor, id_projeto_novo, horas_supervisor, now(), now());
        SET @horas_livres_supervisor = horas_livres_supervisor - horas_supervisor;
        UPDATE tbl_funcionarios
            SET @horas_livres = horas_livres_supervisor
            WHERE id = supervisor;
    END IF;
END;