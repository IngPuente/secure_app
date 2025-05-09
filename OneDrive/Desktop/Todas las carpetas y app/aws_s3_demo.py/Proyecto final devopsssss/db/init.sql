-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS devopsproyectofinal;
USE devopsproyectofinal;

-- Crear la tabla de usuarios (solo una vez, sin repetir)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL UNIQUE,
    contraseña_hash VARCHAR(255) NOT NULL
);

-- Crear la tabla de datos personales con todas las columnas de una vez
CREATE TABLE IF NOT EXISTS datos_personales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre_encriptado VARCHAR(255) NOT NULL,
    direccion_encriptado VARCHAR(255) NOT NULL,
    telefono_encriptado VARCHAR(255) NOT NULL,
    correo_encriptado VARCHAR(255),
    fecha_nacimiento_encriptado VARCHAR(255),
    genero_encriptado VARCHAR(255),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);
