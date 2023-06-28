CREATE DATABASE IF NOT EXISTS proyectov1;
USE proyectov1;

CREATE TABLE IF NOT EXISTS Estado (
    Id_Estado INT,
    Operativo VARCHAR(10),
    Low_battery VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS DispositivosSRL (
    Number_serial INT PRIMARY KEY NOT NULL,
    Modelo VARCHAR(20) NOT NULL,
    Direccion_instalacion VARCHAR(20) NOT NULL,
    Fecha_Instalacion DATE NOT NULL,
    Coordenadas VARCHAR(20) NOT NULL,
    Id_Estado INT NOT NULL,
    FOREIGN KEY (Id_Estado) REFERENCES Estado (Id_Estado)
);

SHOW TABLES;






