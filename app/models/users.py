from pydantic import BaseModel

class UserInput(BaseModel):
    nombre: str
    clave: str
