import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste":True, "num_aleatorio": random.randint(0, 40000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

@app.patch("/estudantes/activate/{id_estudante}")
async def activate_estudante(id_estudante: int):
    return {"id": id_estudante, "ativo": True}

@app.patch("/estudantes/deactivate/{id_estudante}")
async def deactivate_estudante(id_estudante: int):
    return {"id": id_estudante, "ativo": False}

@app.get("/estudantes/getByName")
async def getByName_estudante(nome: str):
    return nome

@app.get("/estudantes/getAll")
async def getAll():
    estudantes = [
        {"name": "Maria", "curso": "Análise e Desenvolvimento de Sistemas", "ativo": True},
        {"name": "João", "curso": "Gestão de Tecnologia da Informação", "ativo": True},
        {"name": "José", "curso": "Sistemas de Informação", "ativo": False}
    ]
    return estudantes

@app.get("/cursos")
async def getCursos():
    cursos = ["Sistemas de Informação", "Engenharia de Software", "Gestão de Tecnologia da Informação", "Análise e Desenvolvimento de Sistemas"]
    return {"cursos": cursos}