from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()


@app.get("/available")
def read_root():
    return {"status": "up"}


class GenerateInputBean(BaseModel):
    prompt: str


@app.post("/generate")
def read_item(bean: GenerateInputBean):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama2",
        "prompt": bean.prompt,
        "stream": False
    })

    return res.json()
