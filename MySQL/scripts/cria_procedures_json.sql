USE empresa;

CREATE PROCEDURE usp_Insere_Departamento_JSON(IN json_info JSON)
BEGIN
    SET @nome = (SELECT JSON_EXTRACT(json_info, '$.nome'));
    CALL usp_Insere_Departamento(@nome);
END;

CREATE PROCEDURE usp_Insere_Funcionario_JSON(IN json_info JSON)
BEGIN
    SET @nome = (SELECT JSON_EXTRACT(json_info, '$.nome'));
    SET @cpf = (SELECT JSON_EXTRACT(json_info, '$.cpf'));
    SET @rg = (SELECT JSON_EXTRACT(json_info, '$.rg'));
    SET @sexo = (SELECT JSON_EXTRACT(json_info, '$.sexo'));
    SET @nascimento = (SELECT JSON_EXTRACT(json_info, '$.nascimento'));
    SET @nascimento = (SELECT DATE(@nascimento));
    SET @possui_cnh = (SELECT JSON_EXTRACT(json_info, '$.possui_cnh'));
    SET @salario = (SELECT JSON_EXTRACT(json_info, '$.salario'));
    SET @departamento = (SELECT JSON_EXTRACT(json_info, '$.departamento'));
    SET @carga_horaria = (SELECT JSON_EXTRACT(json_info, '$.carga_horaria'));
    CALL usp_Insere_Funcionario(@nome, @cpf, @rg, @sexo, @nascimento, @possui_cnh, @salario, @departamento, @carga_horaria);
END;

CREATE PROCEDURE usp_Insere_Projeto_JSON(IN json_info JSON)
BEGIN
    SET @nome_projeto = (SELECT JSON_EXTRACT(json_info, '$.nome_projeto'));
    SET @departamento = (SELECT JSON_EXTRACT(json_info, '$.departamento'));
    SET @horas_necessarias = (SELECT JSON_EXTRACT(json_info, '$.horas_necessarias'));
    SET @supervisor = (SELECT JSON_EXTRACT(json_info, '$.supervisor'));
    SET @horas_supervisao = (SELECT JSON_EXTRACT(json_info, '$.horas_supervisao'));
    CALL usp_Insere_Projeto(@nome_projeto, @departamento, @horas_necessarias, @supervisor, @horas_supervisao);
END;

CREATE PROCEDURE usp_Troca_Supervisor_Projeto_JSON(IN json_info JSON)
BEGIN
    SET @projeto = (SELECT JSON_EXTRACT(json_info, '$.projeto'));
    SET @novo_supervisor = (SELECT JSON_EXTRACT(json_info, '$.novo_supervisor'));
    CALL usp_Troca_Supervisor_Projeto(@projeto, @novo_supervisor);
END;

CREATE PROCEDURE usp_Insere_Funcionario_Projeto_JSON(IN json_info JSON)
BEGIN
    SET @funcionario = (SELECT JSON_EXTRACT(json_info, '$.funcionario'));
    SET @projeto = (SELECT JSON_EXTRACT(json_info, '$.projeto'));
    SET @horas = (SELECT JSON_EXTRACT(json_info, '$.horas'));
    CALL usp_Insere_Funcionario_Projeto(@funcionario, @projeto, @horas);
END;

CREATE PROCEDURE usp_Retira_Funcionario_Projeto_JSON(IN json_info JSON)
BEGIN
    SET @funcionario = (SELECT JSON_EXTRACT(json_info, '$.funcionario'));
    SET @projeto = (SELECT JSON_EXTRACT(json_info, '$.projeto'));
    CALL usp_Retira_Funcionario_Projeto(@funcionario, @projeto);
END;

CREATE PROCEDURE usp_Calcula_Prazo_Estimado_JSON(IN json_info JSON)
BEGIN
    SET @projeto = (SELECT JSON_EXTRACT(json_info, '$.projeto'));
    CALL usp_Calcula_Prazo_Estimado(@projeto);
END;