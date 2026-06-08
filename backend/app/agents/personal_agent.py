from app.utils.llm import generate_response
from app.memory.memory_manager import load_memory


def personal_agent(message: str):
    memory = load_memory()

    recent_memory = memory[-3:] if memory else []

    prompt = f"""
You are a helpful Personal Assistant AI.

Use this recent memory only if it is relevant:
{recent_memory}

User message:
{message}

Answer briefly and clearly.
"""

    return generate_response(prompt)
