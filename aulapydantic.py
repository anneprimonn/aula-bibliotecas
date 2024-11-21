from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    sexo:str
    idade:int
usuario = Usuario(nome = "Joao", sexo='Homem',idade=30)
print(usuario.nome)
print(usuario.sexo)
print(usuario.idade)