from fastapi import APIRouter, HTTPException, Request
from app.config.db import obtener_conexion
from app.models.books import BookInput, BookUpdate

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/")
async def crear_libro(datos: BookInput):
    conn = obtener_conexion()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO libros (titulo, autor, anio) VALUES (%s, %s, %s) RETURNING id",
                (datos.titulo, datos.autor, datos.anio)
            )
            nuevo_id = cursor.fetchone()["id"]
        conn.commit()
    finally:
        conn.close()

    return {"mensaje": "El libro con id " + str(nuevo_id) + " guardado con éxito", "id": nuevo_id}

@router.get("/")
def listar_libros():
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM libros")
            resultados = cursor.fetchall()
    finally:
        conn.close()

    return resultados

@router.put("/{libro_id}")
def actualizar_anio_libro(libro_id: int, datos: BookUpdate):
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM libros WHERE id = %s", (libro_id,))
            if cursor.fetchone() is None:
                conn.close()
                raise HTTPException(status_code=404, detail="El libro solicitado no existe.")
                
            
            cursor.execute("UPDATE libros SET anio = %s WHERE id = %s", (datos.anio, libro_id))
        conn.commit()
    finally:
        conn.close()
    
    return {"mensaje": f"El año de lanzamiento del libro {libro_id} ha sido actualizado"}

@router.delete("/{libro_id}")
def borrar_archivo_del_sistema(libro_id: int):
    conn = obtener_conexion()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
            
            # Inspeccionamos si la orden afectó a alguna fila en el mundo real
            if cursor.rowcount == 0:
                conn.close()
                raise HTTPException(status_code=404, detail="Operación fallida. El libro no existe.")
        
        conn.commit()
    finally:
        conn.close()
    
    # Devolveremos la confirmación triunfante
    return {"mensaje": "El libro ha sido purgado del catálogo de manera irreversible."}