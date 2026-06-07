from fastapi import FastAPI

from app.schemas.chat import ChatRequest
from app.utils.router import route_query

app = FastAPI(
    title="Multi-Agent AI Career & Research Assistant"
)


@app.get("/")
def root():
    return {
        "message": "Project 3 Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = route_query(request.message)

    return {
        "response": result["message"],
        "agent": result["agent"]
    }
