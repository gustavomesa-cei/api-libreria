from fastapi import FastAPI
from app.routers import books
from app.config.db import inicializar_bd

inicializar_bd()  # Inicializamos la base de datos al iniciar la aplicación

app = FastAPI(title="Librería API", description="API para gestionar libros en una biblioteca", version="1.0.0")

app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
