HW_3 SQL

Подключитесь к своей базе данных
SQL запросы и скрин диаграммы выгрузить на GitHub


 1. Создайте базу
      - У каждой таблицы должно быть поле id
      - id автоинкрементальный и является первичным ключом

CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    firstname varchar (50) not null,
    age int not null,
    sex varchar (30) not null
);
CREATE table salary(
     id SERIAL PRIMARY KEY,
     month_salary int
);
CREATE TABLE people_salary(
      id SERIAL PRIMARY KEY,
      people_id int,
      salary_id int,
      foreign key(people_id)
         references people(id),
      foreign key(salary_id)
         references salary(id)
); 
CREATE TABLE passport (
    id SERIAL PRIMARY KEY,
    series int not null,
    number_p int not null,
    code_p int not null,
    people_id int not null,
    foreign key(people_id)
      references people(id)
);

CREATE TABLE cars(
    id SERIAL PRIMARY KEY,
    model varchar (30) not null,
    color varchar (30) not null,
    year_issue int not null,
    owner_name varchar (30) not null,
     foreign key(owner_name) 
       REFERENCES people(firstname)
 );
 2. Заполните таблицы данными. Не менее 10 строк в каждой таблице
INSERT INTO people (firstname,age,sex) VALUES ('Ivan', 23, 'male');
INSERT INTO people (firstname,age,sex) VALUES ('Ivan',14, 'male');
INSERT INTO people (firstname,age,sex) VALUES ('Vika',  45, 'female');
INSERT INTO people (firstname,age,sex) VALUES ('Irina', 26, 'female');
INSERT INTO people (firstname,age,sex) VALUES ('Kate', 35, 'female');
INSERT INTO people (firstname,age,sex) VALUES ('Irina', 26, 'female');
INSERT INTO people (firstname,age,sex) VALUES ('Vadim', 33, 'male');
INSERT INTO people (firstname,age,sex) VALUES ('Sergey', 23, 'male');
INSERT INTO people (firstname,age,sex) VALUES ('Olga', 18, 'female');
INSERT INTO people (firstname,age,sex) VALUES ('Elena', 29, 'female');

INSERT INTO salary(month_salary)VALUES (1000);
INSERT INTO salary(month_salary)VALUES (1200);
INSERT INTO salary(month_salary)VALUES (700);
INSERT INTO salary(month_salary)VALUES (1100);
INSERT INTO salary(month_salary)VALUES (2000);
INSERT INTO salary(month_salary)VALUES (50000);
INSERT INTO salary(month_salary)VALUES (35000);
INSERT INTO salary(month_salary)VALUES (1200);
INSERT INTO salary(month_salary)VALUES (1000);
INSERT INTO salary(month_salary)VALUES (44000);

INSERT INTO people_salary(people_id,salary_id)VALUES (1,1);
INSERT INTO people_salary(people_id,salary_id)VALUES (2,2);
INSERT INTO people_salary(people_id,salary_id)VALUES (3,3);
INSERT INTO people_salary(people_id,salary_id)VALUES (4,4);
INSERT INTO people_salary(people_id,salary_id)VALUES (5,5);
INSERT INTO people_salary(people_id,salary_id)VALUES (6,6);
INSERT INTO people_salary(people_id,salary_id)VALUES (7,7);
INSERT INTO people_salary(people_id,salary_id)VALUES (8,8);
INSERT INTO people_salary(people_id,salary_id)VALUES (9,9);
INSERT INTO people_salary(people_id,salary_id)VALUES (10,10);

INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4007, 1234, 753568, 1);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4000, 3456, 783098, 2);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4034, 5646, 745567, 3);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4001, 3423, 743698, 4);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4023, 0987, 345113, 5);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4566, 3345, 345456, 6);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4478, 3325, 345130, 7);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4109, 4745, 892236, 8);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4226, 3785, 235456, 9);
INSERT INTO passport (series, number_p, code_p, people_id) VALUES (4998, 0145, 785096, 10);


INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('bmw', 'black', 2019, 'Ivan');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('audi', 'red', 1999, 'Ivan');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('lada', 'white', 1998, 'Vika');
INSERT INTO cars (model, color, year_issue, owner_name)values ('maseratti', 'yellow', 2017, 'Irina');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('volvo', 'white', 2002, 'Kate');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('Porsche', 'blue', 2017, 'Irina');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('volvo', 'red', 2015, 'Vadim');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('audi', 'blue', 2000, 'Sergey');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('Honda', 'white', 2014, 'Olga');
INSERT INTO cars (model, color, year_issue, owner_name)VALUES ('bmw', 'black', 2020, 'Elena');


 3. Добавить таблицу X с полями id, name:
CREATE TABLE cars_incurance(
      id SERIAL PRIMARY KEY,
      name varchar (50)
);
 4. Добавить 10 строк  в таблицу X:
INSERT INTO cars_incurance(name) VALUES ('OSAGO');
INSERT INTO cars_incurance(name)VALUES ('CASCO');
INSERT INTO cars_incurance(name)VALUES ('OSAGO');
INSERT INTO cars_incurance(name)VALUES ('CASCO');
INSERT INTO cars_incurance(name)VALUES ('Green_map');
INSERT INTO cars_incurance(name)VALUES ('OSAGO');
INSERT INTO cars_incurance(name)VALUES ('OSAGO');
INSERT INTO cars_incurance(name)VALUES ('Green_map');
INSERT INTO cars_incurance(name)VALUES ('OSAGO');
INSERT INTO cars_incurance(name)VALUES ('CASCO');

 5. Обновить таблицу Y . Добавить поле Y_id которое связано с полем id в таблице X:
ALTER TABLE cars add column owner_id int,
       add foreign key(owner_id) 
       REFERENCES cars_incurance(id);

 6. Обновить таблицу. Добавить varchar поле surname на 50 символов.
ALTER TABLE people add column surname varchar(50);

 7. Обновить таблицу Salary. Добавить varchar поле currency на 7 символов.
ALTER TABLE salary add column currency varchar(7);