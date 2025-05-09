import mysql.connector
import hashlib
from cryptography.fernet import Fernet
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# === Conexión a la base de datos ===
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pato1010",  # ← Si tienes contraseña, ponla aquí
    database="SecureDB"
)
cursor = db.cursor()

# === Llave de encriptación (IMPORTANTE: Guarda esta llave de forma segura) ===
key = Fernet.generate_key()
fernet = Fernet(key)

# === Funciones de encriptación y desencriptación ===
def encrypt(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt(data):
    return fernet.decrypt(data.encode()).decode()

# === Función para registrar usuario ===
def registrar_usuario():
    print(Fore.CYAN + "\n=== Registro de usuario ===")
    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if not usuario or not contraseña:
        print(Fore.RED + "⚠️  Usuario y contraseña no pueden estar vacíos.")
        return

    contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()

    try:
        cursor.execute("INSERT INTO usuarios (usuario, contraseña_hash) VALUES (%s, %s)", (usuario, contraseña_hash))
        db.commit()
        print(Fore.GREEN + "✅ Usuario registrado correctamente.")
    except mysql.connector.IntegrityError:
        print(Fore.RED + "⚠️  El nombre de usuario ya existe.")

# === Función para iniciar sesión ===
def iniciar_sesion():
    print(Fore.CYAN + "\n=== Iniciar sesión ===")
    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()

    cursor.execute("SELECT id FROM usuarios WHERE usuario = %s AND contraseña_hash = %s", (usuario, contraseña_hash))
    result = cursor.fetchone()

    if result:
        print(Fore.GREEN + "✅ Inicio de sesión exitoso.")
        return result[0]  # id_usuario
    else:
        print(Fore.RED + "⚠️  Credenciales incorrectas.")
        return None

# === Función para insertar datos personales ===
def insertar_datos(id_usuario):
    print(Fore.CYAN + "\n=== Agregar datos personales ===")
    nombre = input("Nombre completo: ").strip()
    direccion = input("Dirección: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()
    rfc = input("RFC: ").strip()
    curp = input("CURP: ").strip()

    if not all([nombre, direccion, telefono, correo, fecha_nacimiento, rfc, curp]):
        print(Fore.RED + "⚠️  Todos los campos son obligatorios.")
        return

    cursor.execute("""
        INSERT INTO datos_personales 
        (id_usuario, nombre, direccion_encriptado, telefono, correo, fecha_nacimiento, 
         rfc_encriptado, curp_encriptado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        id_usuario, nombre, encrypt(direccion), telefono, correo, fecha_nacimiento,
        encrypt(rfc), encrypt(curp)
    ))
    db.commit()
    print(Fore.GREEN + "✅ Datos personales guardados correctamente.")

# === Función para ver datos personales ===
def ver_datos(id_usuario):
    print(Fore.CYAN + "\n=== Mis datos personales ===")
    cursor.execute("""
        SELECT nombre, direccion_encriptado, telefono, correo, fecha_nacimiento, 
               rfc_encriptado, curp_encriptado
        FROM datos_personales WHERE id_usuario = %s
    """, (id_usuario,))
    result = cursor.fetchone()

    if result:
        nombre, direccion_enc, telefono, correo, fecha_nac, rfc_enc, curp_enc = result
        print(Fore.YELLOW + f"""
Nombre: {nombre}
Dirección: {decrypt(direccion_enc)}
Teléfono: {telefono}
Correo: {correo}
Fecha de nacimiento: {fecha_nac}
RFC: {decrypt(rfc_enc)}
CURP: {decrypt(curp_enc)}
        """)
    else:
        print(Fore.RED + "⚠️  No has registrado tus datos personales.")

# === Menú principal ===
def menu_principal():
    while True:
        print(Fore.MAGENTA + """
=== Menú principal ===
1. Registrar usuario
2. Iniciar sesión
3. Salir
""")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            id_usuario = iniciar_sesion()
            if id_usuario:
                menu_usuario(id_usuario)
        elif opcion == '3':
            print(Fore.CYAN + "👋 Hasta luego.")
            break
        else:
            print(Fore.RED + "⚠️  Opción no válida.")

# === Menú después de iniciar sesión ===
def menu_usuario(id_usuario):
    while True:
        print(Fore.BLUE + """
=== Menú usuario ===
1. Agregar datos personales
2. Ver mis datos
3. Cerrar sesión
""")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            insertar_datos(id_usuario)
        elif opcion == '2':
            ver_datos(id_usuario)
        elif opcion == '3':
            print(Fore.CYAN + "🔒 Sesión cerrada.")
            break
        else:
            print(Fore.RED + "⚠️  Opción no válida.")

# === Iniciar el programa ===
if __name__ == "__main__":
    menu_principal()
