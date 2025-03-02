import random
from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste":True, "num_aleatorio": random.randint(0, 1000)}
