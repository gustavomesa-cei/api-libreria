from fastapi import APIRouter, HTTPException
from app.config.db import obtener_conexion
from app.models.books import BookInput, BookUpdate

# Definimos el router con prefijo y etiqueta
router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/")
async def crear_libro(datos: BookInput):
    # 1. Abrimos conexión y preparamos al trabajador (cursor)
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    # 2. Ejecutamos nuestra SQL de inserción SEGURA parametrizada (?)
    cursor.execute(
        "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)",
        (datos.titulo, datos.autor, datos.anio)
    )
    
    # 3. Guardar firmemente en disco duro los cambios y sacar el ID nuevo
    conn.commit()
    nuevo_id = cursor.lastrowid 
    
    # 4. Despedir educadamente la conexión liberando los recursos de Windows
    conn.close()
    
    # Devolvemos un JSON amigable haciéndole saber al frontend que triunfó.
    return {"mensaje": "Libro guardado con éxito", "id": nuevo_id}

@router.get("/")
def listar_libros():
    conn = obtener_conexion()
    # Traemos todas las filas. Ojo, si la BD pesa 50GB no deberías usar un fetchall(),
    # pero de momento, ¡esto es perfecto!
    resultados = conn.execute("SELECT * FROM libros").fetchall()
    
    conn.close()
    return resultados

@router.put("/{libro_id}")
def actualizar_anio_libro(libro_id: int, datos: BookUpdate):
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    # Primer paso: Ejecutamos un SELECT super ligero que solo pregunte si la ID existe
    cursor.execute("SELECT 1 FROM libros WHERE id = ?", (libro_id,))
    if cursor.fetchone() is None:
        conn.close()
        # Lanzamos el error 404 (Not Found)
        raise HTTPException(status_code=404, detail="El libro solicitado no existe.")
        
    # Si Python llegó aquí, el libro definitivamente existe. Sobreescribimos con UPDATE
    cursor.execute("UPDATE libros SET anio = ? WHERE id = ?", (datos.anio, libro_id))
    conn.commit()
    conn.close()
    
    return {"mensaje": f"El año de lanzamiento del libro {libro_id} ha sido actualizado"}

@router.delete("/{libro_id}")
def borrar_archivo_del_sistema(libro_id: int):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
    
    # Inspeccionamos si la orden afectó a alguna fila en el mundo real
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Operación fallida. El libro no existe.")
        
    conn.commit()
    conn.close()
    
    # Devolveremos la confirmación triunfante
    return {"mensaje": "El libro ha sido purgado del catálogo de manera irreversible."}