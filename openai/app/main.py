from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)


@app.get("/available")
def read_root():
    return {"status": "up"}


class GenerateInputBean(BaseModel):
    prompt: str


@app.post("/generate")
def generate(bean: GenerateInputBean):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": bean.prompt}]
    )

    return chat_completion
