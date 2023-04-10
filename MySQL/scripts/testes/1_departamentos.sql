USE empresa;

SET @departamento_1 = JSON_SET('{}',
    '$.nome', 'Financeiro'
);

SET @departamento_2 = JSON_SET('{}',
    '$.nome', 'Desenvolvimento Web'
);

SET @departamento_3 = JSON_SET('{}',
    '$.nome', 'Internet das Coisas'
);

SET @departamento_4 = JSON_SET('{}',
    '$.nome', 'Desenvolvimento Web'
);

-- Sucesso
CALL usp_Insere_Departamento_JSON(@departamento_1);
CALL usp_Insere_Departamento_JSON(@departamento_2);
CALL usp_Insere_Departamento_JSON(@departamento_3);

-- Não será executada
CALL usp_Insere_Departamento_JSON(@departamento_4);