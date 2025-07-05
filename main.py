from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class Prompt(BaseModel):
    text: str

# Load Promptist pipeline
pipe = pipeline("text2text-generation", model="microsoft/promptist")

@app.post("/enhance")
async def enhance_prompt(prompt: Prompt):
    output = pipe(prompt.text, max_length=512)[0]["generated_text"]
    return {"improved_prompt": output}
    