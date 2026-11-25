from fastapi import FastAPI
from app.routers import books
from app.routers import users
from app.config.db import inicializar_bd
from app.middleware.cors import setup_cors
from app.middleware.authentication import JWTAuthMiddleware

inicializar_bd()  # Inicializamos la base de datos al iniciar la aplicación

app = FastAPI(title="Librería API", description="API para gestionar libros en una biblioteca", version="1.0.0")

setup_cors(app)
app.add_middleware(JWTAuthMiddleware)

app.include_router(users.router)
app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
