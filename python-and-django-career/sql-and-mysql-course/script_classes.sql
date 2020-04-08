-- 
show databases;

SHOW warnings;

use platzi_operation;

show tables;

select database();

describe authors;
desc books;

show full columns from books;

-- DDL

CREATE database platzi_operation;

CREATE DATABASE IF NOT EXISTS platzi_operation;

CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    author_id INTEGER UNSIGNED,
    title VARCHAR(100) NOT NULL,
    `year` INTEGER UNSIGNED NOT NULL DEFAULT 1900,
    `language` VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 639-1 Language',
    `cover_url` VARCHAR(500),
    price DOUBLE(6,2) NOT NULL DEFAULT 10.0,
    sellable TINYINT DEFAULT 1,
    copies INTEGER NOT NULL DEFAULT 1,
    description TEXT
);

CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(3)
);

CONSTRAINT FOREIGN KEY (attr1) REFERENCES `other_table_name` (`other_table_name_PK`)
CONSTRAINT FOREIGN KEY (author_id) REFERENCES `authors` (`author_id`)

-- DATETIME puede almacenar cualquier fecha incluso antes de 1970
-- TIMESTAMP esta guardado en segundos desde el inicio 
-- de las computadoras (1970) hasta la epoca
-- TIMESTAMP no puede hacer todas las cosas del DATETIME pero 
-- el TIME STAMP es mas rapido y mas eficiente se guarda en segundos.

CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    birthdate DATETIME, 
    gender ENUM('M', 'F', 'ND') NOT NULL,
    active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS operations (
    operation_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    book_id INTEGER UNSIGNED,
    client_id INTEGER UNSIGNED],
    `type` ENUM('P', devuelto, vendido),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
    finished TINYINT(1) NOT NULL,
);

INSERT INTO authors (author_id, name, nationality)
VALUES (NULL,'Juan Rulfo', 'MEX');

INSERT INTO authors(name, nationality)
VALUES ('Gabriel Garcia Márquez', 'COL');

INSERT INTO authors
VALUES (NULL, 'Juan Gabriel Vasquez', 'COL');

INSERT INTO authors (name, nationality)
VALUES ('Julio Cortázar', 'ARG'),
    ('Isabel Allende', 'CHI'),
    ('Octavio Paz', 'MEX'),
    ('Juan Carlos Onetti', 'URU');
    
INSERT INTO authors(author_id, name) values(16, 'Pablo Neruda');

INSERT INTO `clients` (client_id, name, email, birthdate, gender, active)
VALUES (1,'Maria Dolores Gomez','Maria Dolores.95983222J@random.names','1971-06-06','F',1),
(2,'Adrian Fernandez','Adrian.55818851J@random.names','1970-04-09','M',1),
(3,'Maria Luisa Marin','Maria Luisa.83726282A@random.names','1957-07-30','F',1),
(4,'Pedro Sanchez','Pedro.78522059J@random.names','1992-01-31','M',1);

INSERT INTO `clients` (name, email, birthdate, gender, active)
VALUES 
('Pedro Sanchez','Pedro.78522059J@random.names','1992-01-31','M',0)
-- ON DUPLICATE KEY IGNORE ALL -- no lo utilicen, ignora el error y ejecuta lo que sea. 
ON DUPLICATE KEY UPDATE active = VALUES(active);

select * from clients where client_id=4\G

select * from authors where name = 'Octavio Paz'

INSERT INTO books (title, author_id)
VALUES ('El Laberinto de la Soledad', 6);

INSERT INTO books (title, author_id, `year`)
VALUES ('Vuelta al Laberinto de la Soledad',
    (SELECT author_id FROM authors
    WHERE name = 'Octavio Paz'
    LIMIT 1
    ), 1960
);

-- work with files sql  CMD
mysql -u root -p < script.sql
mysql -u root -p -D name_database < script.sql

select name, email, gender from clients LIMIT 10;
select name, email, gender from clients where gender = 'F';
SELECT birthdate FROM clients;
SELECT YEAR(birthdate) FROM clients LIMIT 10;
SELECT NOW();
SELECT YEAR(NOW());
SELECT YEAR(NOW()) - YEAR(birthdate) FROM clients LIMIT 10;

SELECT name, YEAR(NOW()) - YEAR(birthdate) FROM clients 
WHERE name LIKE '%Saave%'
LIMIT 10;

SELECT name, email, YEAR(NOW()) - YEAR(birthdate) AS edad, gender 
FROM clients 
WHERE gender = 'F'
    AND name LIKE '%Lop%'
LIMIT 10;

select count(*) from authors;

select * from authors where author_id > 0 and author_id <= 5;

select * from books where author_id between 1 and 5;

select book_id, author_id, title from books where author_id between 1 and 5;

-- INNER JOIN 
SELECT b.book_id, a.name, a.author_id, b.title
FROM books AS b 
JOIN authors AS a 
    ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5;

SELECT name FROM authors where author_id =4;

DESC transactions;

SELECT * FROM transactions; 

SELECT c.name, b.title, t.type 
FROM transactions AS t
JOIN books AS b
    ON t.book_id = b.book_id
JOIN clients AS c
    ON t.client_id = c.client_id
JOIN authors AS a 
    ON b.author_id = a.author_id
WHERE c.gender = 'F'    
    AND t.type IN ('sell', 'lend')
;

SELECT b.title, a.name
FROM authors AS a, books AS b
where a.author_id = b.author_id
LIMIT 10;
-- LEFT JOIN 

SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a 
LEFT JOIN books AS b 
    ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id;

SELECT a.author_id, a.name, a.nationality, COUNT(b.book_id)
FROM authors AS a 
LEFT JOIN books AS b 
    ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
GROUP BY a.author_id
ORDER BY a.author_id;

-- inner join
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n> 
FROM Tabla_A A
INNER JOIN Tabla_B B
ON A.pk = B.pk

-- left join 
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n> 
FROM Tabla_A A
LEFT JOIN Tabla_B B
ON A.pk = B.pk

-- Outer Join
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A A
FULL OUTER JOIN Tabla_B B
ON A.pk = B.pk

-- Left excluding join
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A A
LEFT JOIN Tabla_B B
ON A.pk = B.pk
WHERE B.pk IS NULL

-- Right Excluding join
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A A
RIGHT JOIN Tabla_B B
ON A.pk = B.pk
WHERE A.pk IS NULL

--  Outer excluding join
SELECT <select_list>
FROM Table_A A
FULL OUTER JOIN Table_B B
ON A.Key = B.Key
WHERE A.Key IS NULL OR B.Key IS NULL

-- CASOS DE NEGOCIOS
-- 1. Que nacionalidades hay?
SELECT DISTINCT nationality FROM authors;
SELECT DISTINCT nationality FROM authors ORDER BY nationality;
-- 2. Cuantos escritores hay de cada nacionalidad?
SELECT nationality, COUNT(author_id) AS c_authors
FROM authors
WHERE nationality IS NOT NULL
GROUP BY nationality
ORDER BY c_authors DESC, nationality ASC;

SELECT nationality, COUNT(author_id) AS c_authors
FROM authors
WHERE nationality IS NOT NULL
    AND nationality NOT IN ('RUS', 'AUS')
GROUP BY nationality
ORDER BY c_authors DESC, nationality ASC;

4. Cual es el promedio/desviacion estandar del precio de libros?

SELECT AVG(price) AS prom, stddev(price) AS std
FROM books 

SELECT nationality, 
    COUNT(book_id) AS c_books,
    AVG(price) AS prom, 
    STDDEV(price) AS std
FROM books AS b 
    JOIN authors AS a 
    ON a.author_id = b.author_id
GROUP BY nationality
ORDER BY c_books DESC;

SELECT price, FLOOR(RAND() * (200 - 1 + 1)) + 1
FROM books
WHERE price IS NULL;

UPDATE books
SET price = FLOOR(RAND() * (200 - 1 + 1)) + 1
WHERE price IS NULL;

-- 6. cual es el precio maximo/minimo de un libro?
SELECT MAX(price), MIN(price)
FROM books;

SELECT a.nationality, MAX(price), MIN(price)
FROM books AS b 
JOIN authors AS a 
    ON a.author_id = b.author_id
GROUP BY nationality
; 

-- REPORT
SELECT c.name, t.type, b.title,
    CONCAT(a.name, "  (", a.nationality, ")") AS author
FROM transactions AS t 
LEFT JOIN clients AS c 
    ON c.client_id = t.client_id
LEFT JOIN books AS b 
    ON b.book_id = t.book_id
LEFT JOIN authors AS a 
    ON b.author_id = a.author_id
;

SELECT TO_DAYS(NOW())

SELECT name, TO_DAYS(birthdate) 
FROM clients;

SELECT c.name, t.type, b.title,
    CONCAT(a.name, "  (", a.nationality, ")") AS author,
    TO_DAYS(NOW()) - TO_DAYS(t.created_at) AS ago
FROM transactions AS t 
LEFT JOIN clients AS c 
    ON c.client_id = t.client_id
LEFT JOIN books AS b 
    ON b.book_id = t.book_id
LEFT JOIN authors AS a 
    ON b.author_id = a.author_id
;

-- Comandos UPDATE Y DELETE
SELECT * FROM authors ORDER BY rand() LIMIT 10;

SELECT COUNT(*) FROM authors;

DELETE 
FROM authors 
WHERE author_id = 161 
LIMIT 1;

SELECT client_id, name FROM clients WHERE active <> 1;

SELECT client_id, name, active, email FROM clients 
WHERE client_id IN (80, 65, 76, 1, 61, 7, 19, 97);

UPDATE clients
SET active = 0
WHERE client_id = 80
LIMIT 1;

UPDATE clients
SET active = 0
WHERE client_id IN (1, 6, 8, 27, 90)
    OR name like '%Lopez%';

SELECT * 
FROM clients
WHERE client_id IN (1, 6, 8, 27, 90)
    OR name like '%Lopez%';

TRUNCATE TABLE transactions;

SELECT DISTINCT nationality FROM authors;

UPDATE authors
SET nationality  = 'GBR'
WHERE nationality = 'ENG';

-- Super Querys
SELECT COUNT(book_id) FROM books;

SELECT COUNT(book_id), SUM(1) FROM books;

SELECT SUM(price) FROM books WHERE sellable = 1;

SELECT SUM(price * copies) FROM books WHERE sellable = 1;

SELECT sellable, SUM(price * copies) 
FROM books 
GROUP BY sellable;

select book_id, sellable from books where sellable = 1 order by rand() LIMIT 10;

UPDATE books 
SET sellable = 0 
WHERE book_id IN (42, 59, 66, 140, 186);

SELECT COUNT(book_id), 
    SUM(IF(YEAR < 1950, 1, 0)) AS '<1950',
    SUM(IF(YEAR >= 1950 AND YEAR < 1990, 1, 0)) AS '<1990',
    SUM(IF(YEAR >= 1990 AND YEAR < 2000, 1, 0)) AS '<2000',
    SUM(IF(YEAR >= 2000, 1, 0)) AS '<HOY'
FROM books;

SELECT a.nationality, 
    COUNT(book_id), 
    SUM(IF(YEAR < 1950, 1, 0)) AS '<1950',
    SUM(IF(YEAR >= 1950 AND YEAR < 1990, 1, 0)) AS '<1990',
    SUM(IF(YEAR >= 1990 AND YEAR < 2000, 1, 0)) AS '<2000',
    SUM(IF(YEAR >= 2000, 1, 0)) AS '<HOY'
FROM books AS b
JOIN authors AS a
    ON a.author_id = b.author_id
WHERE a.nationality IS NOT NULL
GROUP BY nationality
;

-- Comando mysqldump

ALTER TABLE authors
ADD COLUMN birthyear INTEGER first;

ALTER TABLE authors
ADD COLUMN birthyear 
INTEGER DEFAULT 1930 
AFTER name;

-- cambia de entero a year y el default 1920
ALTER TABLE authors
MODIFY COLUMN birthyear year default 1920;

ALTER TABLE authors DROP COLUMN birthyear;

show tables like '%i%';

-- backup
-- write in the console CMD
--mysqldump -u root -p pruebaplatzi --host
-- all database with data
mysqldump -u root -p pruebaplatzi 
-- only schema 
mysqldump -u root -p -d pruebaplatzi 
-- only schema on file 
mysqldump -u root -p -d pruebaplatzi > eschema.sql
mysqldump -u root -p -d pruebaplatzi > d:/eschema.sql

