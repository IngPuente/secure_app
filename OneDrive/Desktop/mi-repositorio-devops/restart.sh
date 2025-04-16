#!/bin/bash

echo "Deteniendo contenedor..."
docker-compose down

echo "Reconstruyendo contenedor..."
docker-compose build

echo "Iniciando contenedor..."
docker-compose up -d

echo "Aplicación reiniciada correctamente 🚀"

chmod +x restart.sh

