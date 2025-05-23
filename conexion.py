import mysql.connector
from mysql.connector import Error

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host='localhost',        # Cambia esto si tu base no está en localhost
            user='root',       # Reemplaza con tu usuario MySQL
            password='',# Reemplaza con tu contraseña
            database='registro_civil'  # Reemplaza con el nombre de tu base de datos
        )

        if conexion.is_connected():
            print("✅ Conexión exitosa. Desde Nol")
            return conexion

    except Error as e:
        print(f"❌ Error al conectar: {e}")
        return None

conexion = conectar_base_datos()

if conexion:
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES;")
    for tabla in cursor.fetchall():
        print(f"📄 Tabla: {tabla[0]}")

    cursor.close()
    conexion.close()
    print("🔒 Conexión cerrada.")
