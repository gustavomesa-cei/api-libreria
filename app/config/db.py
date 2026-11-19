import psycopg2
from psycopg2.extras import RealDictCursor


def obtener_conexion():
    conexion = psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password="npg_57svCDhealJR",
        host="ep-summer-darkness-be84rbv6-pooler.c-9.us-east-2.aws.neon.tech",
        port="5432",
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
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    anio INTEGER
                )
            """)
        conn.commit()  # Guarda los cambios en la base de datos
    finally:
        conn.close()  # Cierra la conexión siempre al terminar