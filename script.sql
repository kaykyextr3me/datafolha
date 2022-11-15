create database datafodas;

use datafodas;

CREATE TABLE cadastro_candidato (
  id int primary key auto_increment not NULL,
  numero int NOT NULL,
  nome varchar(64) NOT NULL,
  partido varchar(64) NOT NULL,
  cargo varchar(64) NOT NULL,
  regiao varchar(64) NOT NULL,
  naturalidade varchar(64) NOT NULL,
  genero char(1)
);


CREATE TABLE voto(
	qtd_votos int primary key auto_increment,
	id_candidato int not null,
	FOREIGN key (id_candidato) REFERENCES cadastro_candidato(id)
);


use datafodas;
create table administrador(
	id integer primary key auto_increment,
    nome_login varchar(64),
    senha varchar(128)
);

insert into administrador (nome_login, senha)
values ("admin", "123");

select * from administrador;

select * from cadastro_candidato;



