USE empresa;

-- Insere um novo departamento na respectiva tabela
CREATE PROCEDURE usp_Insere_Departamento(IN nome_dpto VARCHAR(50))
    BEGIN
        INSERT INTO tbl_departamentos (nome, data_criacao, data_atualizacao)
            VALUES (nome_dpto, now(), now());
    END;

-- Cadastra um novo funcionário
CREATE PROCEDURE usp_Insere_Funcionario (IN nome varchar(50), IN cpf varchar(11), in rg varchar(9), in sexo int, IN nascimento date, in possui_cnh boolean, IN salario float, in departamento int, in carga_horaria int)
BEGIN
    INSERT INTO tbl_funcionarios (nome, cpf, rg, sexo_id, nascimento, possui_cnh, salario, departamento_id, carga_horaria_semanal, horas_livres, data_criacao, data_atualizacao)
    VALUES (nome, cpf, rg, sexo, nascimento, possui_cnh, salario, departamento, carga_horaria, carga_horaria, now(), now());
END;

CREATE PROCEDURE usp_Aumenta_Carga_Horaria (IN funcionario INT, IN horas INT)
BEGIN
    SET @nova_carga_horaria = (SELECT tf.carga_horaria_semanal FROM tbl_funcionarios tf WHERE tf.id = funcionario) + horas;
    UPDATE tbl_funcionarios tf SET tf.carga_horaria_semanal = @nova_carga_horaria WHERE tf.id = funcionario;
    UPDATE tbl_funcionarios tf SET tf.data_atualizacao = now() WHERE tf.id = funcionario;
END;

-- Reduz a carga horária semanal do funcionário
CREATE PROCEDURE usp_Reduz_Carga_Horaria (IN funcionario INT, IN horas INT)
BEGIN
    SET @nova_carga_horaria = (SELECT tf.carga_horaria_semanal FROM tbl_funcionarios tf WHERE tf.id = funcionario) - horas;
    IF @nova_carga_horaria > 0 THEN
        UPDATE tbl_funcionarios tf SET tf.carga_horaria_semanal = @nova_carga_horaria WHERE tf.id = funcionario;
        UPDATE tbl_funcionarios tf SET tf.data_atualizacao = now() WHERE tf.id = funcionario;
    END IF;
END;

-- Aumenta a quantidade de horas livres do funcionário
CREATE PROCEDURE usp_Aumenta_Horas_Livres (IN funcionario INT, IN horas INT)
BEGIN
    SET @novas_horas_livres = (SELECT tf.horas_livres FROM tbl_funcionarios tf WHERE tf.id = funcionario) + horas;
    SET @carga_horaria_semanal = (SELECT tf.carga_horaria_semanal FROM tbl_funcionarios tf WHERE tf.id = funcionario);
    IF @novas_horas_livres <= @carga_horaria_semanal THEN
        UPDATE tbl_funcionarios tf SET tf.horas_livres = @novas_horas_livres WHERE tf.id = funcionario;
        UPDATE tbl_funcionarios tf SET tf.data_atualizacao = now() WHERE tf.id = funcionario;
    END IF;
END;

-- Diminui a quantidade de horas livres do funcionário
CREATE PROCEDURE usp_Reduz_Horas_Livres (IN funcionario INT, IN horas INT)
BEGIN
    SET @novas_horas_livres = (SELECT tf.horas_livres FROM tbl_funcionarios tf WHERE tf.id = funcionario) - horas;
    IF @novas_horas_livres >= 0 THEN
        UPDATE tbl_funcionarios tf SET tf.horas_livres = @novas_horas_livres WHERE tf.id = funcionario;
        UPDATE tbl_funcionarios tf SET tf.data_atualizacao = now() WHERE tf.id = funcionario;
    END IF;    
END;

-- Cria um novo projeto. O projeto será criado apenas se o supervisor desejado possuir as horas livres.
CREATE PROCEDURE usp_Insere_Projeto(IN novo_projeto VARCHAR (50), IN id_departamento INT, IN horas INT, IN supervisor INT, IN horas_supervisor INT)
BEGIN
    -- Armazena na variável as horas disponíveis do supervisor
    SET @horas_livres_supervisor = (SELECT tf.horas_livres FROM tbl_funcionarios tf WHERE tf.id = supervisor limit 1);
    
    -- Cria o projeto apenas se o supervisor tiver as horas livres necessárias para supervisão
    IF @horas_livres_supervisor >= horas_supervisor THEN
        INSERT INTO tbl_projetos (departamento_id, nome, horas_necessarias, horas_realizadas, prazo_estimado, ultimo_calculo_hora, supervisor_id, horas_supervisao, data_criacao, data_atualizacao)
            VALUES (id_departamento, novo_projeto, horas, 0, null, CURDATE(), supervisor, horas_supervisor, now(), now());
        CALL usp_Reduz_Horas_Livres(supervisor, horas_supervisor);
    END IF;
END;

-- Troca o Supervisor de um projeto por outro. Só o fará se o novo supervisor tiver horas livres o suficiente
CREATE PROCEDURE usp_Troca_Supervisor_Projeto (IN projeto INT, IN novo_supervisor INT)
BEGIN
    SET @supervisor_antigo = (SELECT tp.supervisor_id FROM tbl_projetos tp WHERE tp.id = projeto);
    IF novo_supervisor != @supervisor_antigo THEN
        SET @horas_livres_novo_supervisor = (SELECT tf.horas_livres FROM tbl_funcionarios tf WHERE tf.id = novo_supervisor);
        SET @horas_supervisao = (SELECT tp.horas_supervisao FROM tbl_projetos tp WHERE tp.id = projeto);
        IF @horas_livres_novo_supervisor >= @horas_supervisao THEN
            UPDATE tbl_projetos tp SET tp.supervisor_id = novo_supervisor WHERE tp.id = projeto;
            UPDATE tbl_projetos tp SET tp.data_atualizacao = now() WHERE tp.id = projeto;
            CALL usp_Reduz_Horas_Livres(novo_supervisor, @horas_supervisao);
            CALL usp_Aumenta_Horas_Livres(@supervisor_antigo, @horas_supervisao);
        END IF;
    END IF;
END;

-- 
CREATE PROCEDURE usp_Insere_Funcionario_Projeto(IN funcionario INT, IN projeto INT, IN horas INT)
BEGIN
    SET @horas_livres_funcionario = (SELECT tf.horas_livres FROM tbl_funcionarios tf WHERE tf.id = funcionario);
    IF @horas_livres_funcionario >= horas THEN
        INSERT INTO tbl_funcionarios_projetos (funcionario_id, projeto_id, horas_trabalhadas, data_criacao, data_atualizacao)
            VALUES (funcionario, projeto, horas, now(), now());
        CALL usp_Reduz_Horas_Livres(funcionario, horas);
    END IF;
END;

CREATE PROCEDURE usp_Retira_Funcionario_Projeto(IN funcionario INT, IN projeto INT)
BEGIN
    SET @horas_no_projeto = (SELECT tfp.horas_trabalhadas FROM tbl_funcionarios_projetos tfp WHERE tfp.funcionario_id = funcionario AND tfp.projeto_id = projeto);
    DELETE FROM tbl_funcionarios_projetos WHERE funcionario_id = funcionario AND projeto_id = projeto;
    CALL usp_Aumenta_Horas_Livres(funcionario, @horas_no_projeto); 
END;

CREATE PROCEDURE usp_Calcula_Prazo_Estimado(IN projeto INT)
BEGIN
    SET @soma_horas_semanais = (SELECT SUM(tfp.horas_trabalhadas) FROM tbl_funcionarios_projetos tfp WHERE tfp.projeto_id = projeto);
    SET @ultimo_calculo = (SELECT tp.ultimo_calculo_hora FROM tbl_projetos WHERE tp.id = projeto);
    SET @dias_apos_ultimo_calculo = (SELECT DATEDIFF(DATE(NOW()), @ultimo_calculo));
    SET @semanas_completas = (SELECT @dias_apos_ultimo_calculo DIV 7);
    SET @horas_realizadas = (SELECT tp.horas_realizadas FROM tbl_projetos tp WHERE tp.id = projeto)
                            + (SELECT @semanas_completas * @soma_horas_semanais);
    UPDATE tbl_projetos tp SET tp.horas_realizadas = horas_realizadas WHERE tp.id = projeto;
    SET @horas_restantes = (SELECT tp.horas_necessarias FROM tbl_projetos tp WHERE tp.id = projeto)
                            - @horas_realizadas;
    SET @semanas_restantes = (SELECT @horas_restantes DIV @soma_horas_semanais);
    SET @dias_restantes = @semanas_restantes * 7;
    SET @novo_prazo = DATE_ADD(@ultimo_calculo, INTERVAL @dias_restantes DAY);
    UPDATE tbl_projetos tp SET tp.prazo_estimado = @novo_prazo WHERE tp.id = projeto;
    UPDATE tbl_projetos tp SET tp.data_atualizacao = now() WHERE tp.id = projeto;
END;