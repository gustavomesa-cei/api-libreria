from fastapi import APIRouter, HTTPException
from app.config.db import obtener_conexion
from app.models.users import UserInput
import bcrypt
import jwt
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register")
async def crear_usuario(datos: UserInput):
    conn = obtener_conexion()
    
    try:
        with conn.cursor() as cursor:
            salt = bcrypt.gensalt()
            contrasenia_hasheada = bcrypt.hashpw(datos.clave.encode('utf-8'), salt)

            cursor.execute(
                "INSERT INTO usuario (nombre, clave) VALUES (%s, %s) RETURNING id",
                (datos.nombre, contrasenia_hasheada.decode('utf-8'))
            )
            nuevo_usuario = {"id": cursor.fetchone()["id"], "nombre": datos.nombre}
        conn.commit()
    finally:
        conn.close()

    return jwt.encode(nuevo_usuario, os.getenv("SECRET_KEY"), algorithm="HS256")
     

@router.post("/login")
async def login_usuario(datos: UserInput):
    conn = obtener_conexion()
    
    try:
        with conn.cursor() as cursor:
            
            cursor.execute(
                "SELECT id, nombre, clave FROM usuario WHERE nombre = %s",
                (datos.nombre,)
            )
            resultado = cursor.fetchone()
            usuario = {"id": resultado["id"], "nombre": resultado["nombre"]} if resultado else None

            if not resultado or not bcrypt.checkpw(datos.clave.encode('utf-8'), resultado["clave"].encode('utf-8')):
                raise HTTPException(status_code=404, detail="Usuario o contraseña incorrectos")

        conn.commit()
    finally:
        conn.close()

    return jwt.encode(usuario, os.getenv("SECRET_KEY"), algorithm="HS256")
