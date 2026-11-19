from pydantic import BaseModel

class BookInput(BaseModel):
    titulo: str
    autor: str
    anio: int

class BookUpdate(BaseModel):
    anio: int