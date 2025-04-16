#!/bin/bash

echo "Instalando dependencias de Python..."
pip install -r requirements.txt

echo "Construyendo imagen Docker..."
docker-compose build

echo "Levantando contenedor..."
docker-compose up -d

echo "Listo! Tu app está corriendo en: http://localhost:5000 🚀"

chmod +x install.sh
