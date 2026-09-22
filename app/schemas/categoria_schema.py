from pydantic import BaseModel, Field

# Realiza registro  
class CategoriaCrear(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)

# Devuelve id y nombre de registro
class CategoriaRespuesta(BaseModel):
    id: int
    nombre: str