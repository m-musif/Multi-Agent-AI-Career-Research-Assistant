from app.memory.memory_manager import load_memory
from app.memory.memory_manager import save_memory
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


@app.get("/memory")
def get_memory():
    return load_memory()

@app.post("/chat")
@app.post("/chat")
def chat(request: ChatRequest):

    result = route_query(request.message)

    save_memory(
        user_message=request.message,
        assistant_response=result["message"]
    )

    return {
        "response": result["message"],
        "agent": result["agent"]
    }
