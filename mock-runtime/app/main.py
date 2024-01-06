from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/available")
def read_root():
    return {"status": "up"}


class GenerateInputBean(BaseModel):
    prompt: str


@app.post("/generate")
def generate(bean: GenerateInputBean):
    return {'response': bean.prompt}
