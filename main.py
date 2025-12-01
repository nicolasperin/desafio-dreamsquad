from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class ChatRequest(BaseModel):
    message:str

@app.post("/chat")
async def chat (request: ChatRequest):
    response = agent(request.message)
    return {"response": response}