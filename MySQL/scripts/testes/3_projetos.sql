USE empresa;

SET @projeto_1 = JSON_SET('{}',
    '$.nome_projeto', 'Sistema de Segurança',
    '$.departamento', 3,
    '$.horas_necessarias', 200,
    '$.supervisor', 1,
    '$.horas_supervisao', 15 
);

SET @projeto_2 = JSON_SET('{}',
    '$.nome_projeto', 'Sistema de Gestão Acadêmica',
    '$.departamento', 2,
    '$.horas_necessarias', 400,
    '$.supervisor', 2,
    '$.horas_supervisao', 20 
);

SET @projeto_3 = JSON_SET('{}',
    '$.nome_projeto', 'Sistema de Documentos',
    '$.departamento', 2,
    '$.horas_necessarias', 150,
    '$.supervisor', 1,
    '$.horas_supervisao', 15 
);

SET @projeto_4 = JSON_SET('{}',
    '$.nome_projeto', 'Sistema de Documentos',
    '$.departamento', 1,
    '$.horas_necessarias', 50,
    '$.supervisor', 1,
    '$.horas_supervisao', 15
);


CALL usp_Insere_Projeto_JSON(@projeto_1);
CALL usp_Insere_Projeto_JSON(@projeto_2);
CALL usp_Insere_Projeto_JSON(@projeto_3);
CALL usp_Insere_Projeto_JSON(@projeto_4);