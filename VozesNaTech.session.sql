delete User (
    id,
    status,
    name,
    email,
    cell_phone,
    ethnicity,
    birth_date,
    female_gender,
    password
  )
VALUES (
    id:int,
    status:int,
    'name:varchar',
    'email:varchar',
    'cell_phone:varchar',
    'ethnicity:varchar',
    'birth_date:date',
    'female_gender:tinyint',
    'password:varchar'
  );DELETE FROM BusinessArea;
INSERT INTO BusinessArea (id, status, name) VALUES
(1, 1, 'Cibersegurança'),
(2, 1, 'Criptomoedas'),
(3, 1, 'Gestão de TI'),
(4, 1, 'Dados'),
(5, 1, 'Programação'),
(6, 1, 'Design/Jogos Digitais'),
(7, 1, 'Inteligência Artificial');
