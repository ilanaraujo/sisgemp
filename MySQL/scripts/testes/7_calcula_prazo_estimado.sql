USE empresa;

SET @ultimo_calculo_1 = DATE_SUB(CURDATE(), INTERVAL 7 DAY);
SET @ultimo_calculo_2 = DATE_SUB(CURDATE(), INTERVAL 14 DAY);
SET @ultimo_calculo_3 = DATE_SUB(CURDATE(), INTERVAL 28 DAY);

UPDATE tbl_projetos tp SET tp.ultimo_calculo_hora = @ultimo_calculo_1 WHERE tp.id = 1;

UPDATE tbl_projetos tp SET tp.ultimo_calculo_hora = @ultimo_calculo_2 WHERE tp.id = 2;

UPDATE tbl_projetos tp SET tp.ultimo_calculo_hora = @ultimo_calculo_3 WHERE tp.id = 3;


SET @projeto_prazo_calculado_1 = JSON_SET('{}',
    '$.projeto', 1
);

SET @projeto_prazo_calculado_2 = JSON_SET('{}',
    '$.projeto', 2
);

SET @projeto_prazo_calculado_3 = JSON_SET('{}',
    '$.projeto', 3
);

CALL usp_Calcula_Prazo_Estimado_JSON(@projeto_prazo_calculado_1);
CALL usp_Calcula_Prazo_Estimado_JSON(@projeto_prazo_calculado_2);
CALL usp_Calcula_Prazo_Estimado_JSON(@projeto_prazo_calculado_3);