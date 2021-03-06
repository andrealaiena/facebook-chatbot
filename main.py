from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chatbot")
async def chatbot(message: str = ""):
    return {"message": f"Hello World, your message was: {message}",
            "timestamp": datetime.now()}