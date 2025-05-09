# SecureApp

Aplicación Python para gestionar usuarios y sus datos personales con encriptación, utilizando MySQL.

## Ejecutar con Docker

```bash
docker-compose up --build


---

## ✅ 3️⃣ Adaptación de tu código (`app/main.py`) para funcionar en Docker (variables de entorno)

Cambia **tu conexión a la base de datos** así 👇

```python
import os
import mysql.connector
import hashlib
from cryptography.fernet import Fernet
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# === Conexión a la base de datos ===
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "pato1010"),
    database=os.getenv("MYSQL_DATABASE", "SecureDB")
)
cursor = db.cursor()
