CREATE DATABASE IF NOT EXISTS projecto_integrador;
use projecto_integrador;

CREATE TABLE if not exists Estado (
Id_Estado int,
Operativo varchar(10),
Low_battery varchar(10)
);

CREATE TABLE if not exists DispositivosSRL(
Number_serial int primary key not null,
Modelo varchar(20) not null,
Direccion_instalacion varchar(20) not null,
Fehca_Instalacion DATE not null,
Coordenadas varchar (20) not null,
Id_Estado int not null,
FOREIGN KEY(Id_Estado) REFERENCES DispositivosSRL(Number_serial)
);
SHOW TABLES;





