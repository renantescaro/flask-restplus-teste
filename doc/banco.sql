CREATE DATABASE testes;


CREATE TABLE pessoas(
	id int not null auto_increment,
    nome varchar(200),
	data_nascimento date,
    
    primary key(id)
);