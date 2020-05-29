create database if not exists cine_db;

use cine_db;


create table if not exists sala (
	id_sala int not null auto_increment,
    nombre_sala varchar(20) not null,
    
    primary key(id_sala)
) engine = InnoDB;

create table if not exists pelicula(
	id_pelicula int not null auto_increment,
    Nombre varchar(200) not null,
    Sinopsis varchar(800) not null,
    categoria varchar(10) not null,
    duracion varchar(20) not null,
    primary key (id_pelicula)
) engine = InnoDB;

create table if not exists funcion(
	id_funcion int not null auto_increment,
    id_pelicula int not null,
    id_sala int not null,
    fecha date not null,
    hora time not null,
    precio float not null,
    idioma varchar(60),
    
    primary key(id_funcion),
    
     constraint fk_pelicula_funcion foreign key(id_pelicula)
		references pelicula(id_pelicula)
        on delete cascade
        on update cascade,
        
	constraint fk_sala_pelicula foreign key(id_sala)
		references sala(id_sala)
        on delete cascade
        on update cascade
	
) engine = Innodb;

create table if not exists asiento (
	id_asiento int not null auto_increment,
    id_sala int not null,
    nombre varchar(5) not null,
    
    primary key (id_asiento),
    
    constraint fk_sala_asiento foreign key(id_sala)
		references sala(id_sala)
        on delete cascade
        on update cascade
);

create table if not exists boleto(
	id_boleto int not null auto_increment,
    id_funcion int not null,
    id_asiento int not null,
    
    primary key (id_boleto),
        
	constraint fk_funcion_boleto foreign key(id_funcion)
		references funcion(id_funcion)
        on delete cascade
        on update cascade,
        
	constraint fk_boleto_asiento foreign key(id_asiento)
		references asiento(id_asiento)
        on delete cascade
        on update cascade
) engine = innodb;

create table if not exists administrador(
	id_admin int not null auto_increment,
    nombre varchar(35) not null,
    apellido_p varchar(35) not null,
    apellido_m varchar(35),
    usuario varchar(35) not null,
    contraseña varchar(20) not null,
    primary key(id_admin)
) engine = InnoDB;

