# Imagen base
FROM python:3.9-slim-bullseye

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar app
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]

