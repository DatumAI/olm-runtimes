import os

from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


def get_internet_access_response_dict():
    try:
        res = requests.get("https://google.com", timeout=5)
        return {"canAccessGoogleInternet": True, 'googleResponseCode': res.status_code}
    except:
        return {"canAccessGoogleInternet": False}


def get_file_access_response_dict():
    file_exists = os.path.isfile('/config.json')
    file_content = None

    if file_exists:
        with open("/config.json", 'r') as f:
            file_content = f.read()

    return {"fileExists": file_exists, 'fileContent': file_content}


@app.get("/available")
def read_root():
    return {"status": "up", **get_internet_access_response_dict(), **get_file_access_response_dict()}


class GenerateInputBean(BaseModel):
    prompt: str


@app.post("/generate")
def generate(bean: GenerateInputBean):
    return {'response': bean.prompt}
