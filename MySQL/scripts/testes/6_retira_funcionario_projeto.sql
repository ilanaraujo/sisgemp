USE empresa;

SET @funcionario_retirado_1 = JSON_SET('{}',
    '$.funcionario', 1,
    '$.projeto', 1
);

SET @funcionario_retirado_2 = JSON_SET('{}',
    '$.funcionario', 1,
    '$.projeto', 3
);

CALL usp_Retira_Funcionario_Projeto_JSON(@funcionario_retirado_1);
CALL usp_Retira_Funcionario_Projeto_JSON(@funcionario_retirado_2);