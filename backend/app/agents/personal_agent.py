from app.utils.llm import generate_response
from app.memory.memory_manager import load_memory


def personal_agent(message: str):

    memory = load_memory()

    prompt = f"""
You are a Personal Assistant AI.

You have access to the user's recent memory:

{memory}

Use this memory only if it is relevant.

Help with:
- Goals
- Productivity
- Planning
- Personal guidance
- Remembering useful information

User:
{message}
"""

    return generate_response(prompt)
