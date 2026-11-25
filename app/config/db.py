import psycopg2
from psycopg2.extras import RealDictCursor
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def obtener_conexion():
    conexion = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        cursor_factory=RealDictCursor, 
    )
    return conexion

def inicializar_bd():
    conn = obtener_conexion()
    try:
        # En psycopg2 las consultas siempre pasan por un cursor
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    id SERIAL PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    anio INTEGER
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id SERIAL PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    clave TEXT NOT NULL
                )
            """)
        conn.commit()  # Guarda los cambios en la base de datos
    finally:
        conn.close()  # Cierra la conexión siempre al terminar