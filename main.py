from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books
from app.config.db import inicializar_bd

inicializar_bd()  # Inicializamos la base de datos al iniciar la aplicación

app = FastAPI(title="Librería API", description="API para gestionar libros en una biblioteca", version="1.0.0")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Or ["*"] to allow all origins
    allow_credentials=True,     # Allow cookies and auth headers
    allow_methods=["*"],        # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],        # Allow all request headers
)

app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
