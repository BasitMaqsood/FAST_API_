from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to Atria Logics': f'{name}'}