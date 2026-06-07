from pydantic import BaseModel


class MemoryItem(BaseModel):
    user_message: str
    assistant_response: str
