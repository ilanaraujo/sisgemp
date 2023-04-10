use empresa;

SET @funcionario_1 = JSON_SET('{}',
    '$.nome', 'João',
    '$.cpf', 12345678910,
    '$.rg', 123456789,
    '$.sexo', 2,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 1234.56,
    '$.departamento', 1,
    '$.carga_horaria', 40
);

SET @funcionario_2 = JSON_SET('{}',
    '$.nome', 'Maria',
    '$.cpf', 10987654321,
    '$.rg', 987654321,
    '$.sexo', 1,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 6543.21,
    '$.departamento', 1,
    '$.carga_horaria', 20
);

SET @funcionario_3 = JSON_SET('{}',
    '$.nome', 'José',
    '$.cpf', 13579246810,
    '$.rg', 135792468,
    '$.sexo', 2,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 0,
    '$.salario', 6543.21,
    '$.departamento', 2,
    '$.carga_horaria', 30
);

SET @funcionario_4 = JSON_SET('{}',
    '$.nome', 'Ana',
    '$.cpf', 24681013579,
    '$.rg', 246813579,
    '$.sexo', 1,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 6543.21,
    '$.departamento', 2,
    '$.carga_horaria', 30
);

SET @funcionario_5 = JSON_SET('{}',
    '$.nome', 'John',
    '$.cpf', 12345123451,
    '$.rg', 123451234,
    '$.sexo', 2,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 7543.21,
    '$.departamento', 2,
    '$.carga_horaria', 30
);

SET @funcionario_6 = JSON_SET('{}',
    '$.nome', 'John',
    '$.cpf', 10101010101,
    '$.rg', 101010101,
    '$.sexo', 2,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 6543.21,
    '$.departamento', 2,
    '$.carga_horaria', 20
);

SET @funcionario_7 = JSON_SET('{}',
    '$.nome', 'Joseph',
    '$.cpf', 12345123451,
    '$.rg', 110011001,
    '$.sexo', 2,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 6543.21,
    '$.departamento', 2,
    '$.carga_horaria', 20
);

SET @funcionario_8 = JSON_SET('{}',
    '$.nome', 'Mary',
    '$.cpf', 11001100110,
    '$.rg', 123451234,
    '$.sexo', 1,
    '$.nascimento', '1990-06-15',
    '$.possui_cnh', 1,
    '$.salario', 6543.21,
    '$.departamento', 2,
    '$.carga_horaria', 20
);


-- Devem ser executadas sem erros
CALL usp_Insere_Funcionario_JSON(@funcionario_1);
CALL usp_Insere_Funcionario_JSON(@funcionario_2);
CALL usp_Insere_Funcionario_JSON(@funcionario_3);
CALL usp_Insere_Funcionario_JSON(@funcionario_4);
CALL usp_Insere_Funcionario_JSON(@funcionario_5);

-- Não serão concluídas
CALL usp_Insere_Funcionario_JSON(@funcionario_6);
CALL usp_Insere_Funcionario_JSON(@funcionario_7);
CALL usp_Insere_Funcionario_JSON(@funcionario_8);