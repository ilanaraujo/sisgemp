USE empresa;

SET @novo_integrante_1 = JSON_SET('{}',
    '$.funcionario', 1,
    '$.projeto', 1,
    '$.horas', 10
);

CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_1);