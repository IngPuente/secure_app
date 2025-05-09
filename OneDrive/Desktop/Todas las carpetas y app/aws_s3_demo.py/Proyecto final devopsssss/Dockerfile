# Imagen base
FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos y dependencias
COPY app/ /app/
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la app
CMD ["python", "main.py"]
