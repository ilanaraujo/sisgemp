USE empresa;

SET @novo_integrante_1 = JSON_SET('{}',
    '$.funcionario', 1,
    '$.projeto', 1,
    '$.horas', 10
);

SET @novo_integrante_2 = JSON_SET('{}',
    '$.funcionario', 1,
    '$.projeto', 2,
    '$.horas', 15
);

SET @novo_integrante_3 = JSON_SET('{}',
    '$.funcionario', 2,
    '$.projeto', 1,
    '$.horas', 1
);

SET @novo_integrante_4 = JSON_SET('{}',
    '$.funcionario', 3,
    '$.projeto', 3,
    '$.horas', 10
);

SET @novo_integrante_5 = JSON_SET('{}',
    '$.funcionario', 4,
    '$.projeto', 1,
    '$.horas', 30
);

SET @novo_integrante_6 = JSON_SET('{}',
    '$.funcionario', 5,
    '$.projeto', 3,
    '$.horas', 25
);

CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_1);
CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_2);
CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_3);
CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_4);
CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_5);
CALL usp_Insere_Funcionario_Projeto_JSON(@novo_integrante_6);
