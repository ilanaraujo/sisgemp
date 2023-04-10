USE empresa;

SET @projeto = JSON_SET('{}',
    '$.projeto', 1,
    '$.novo_supervisor', 3
);

SET @projeto_mesmo_supervisor = JSON_SET('{}',
    '$.projeto', 1,
    '$.novo_supervisor', 3
);

CALL usp_Troca_Supervisor_Projeto_JSON(@projeto);
CALL usp_Troca_Supervisor_Projeto_JSON(@projeto_mesmo_supervisor);