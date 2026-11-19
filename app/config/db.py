import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect("biblioteca_api.db")
    conexion.row_factory = sqlite3.Row 
    return conexion

def inicializar_bd():
    conn = obtener_conexion()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            anio INTEGER
        )
    """)
    conn.commit()
    conn.close()