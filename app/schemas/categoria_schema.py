from pydantic import BaseModel, ConfigDict, Field

#Crear un esquema para la categoria
class CategoriaCrear(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)

#Crear un esquema para la respuesta de la categoria
class CategoriaRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str