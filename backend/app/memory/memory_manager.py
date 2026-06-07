import json
from pathlib import Path


MEMORY_FILE = Path("app/memory/memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return []

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return []


def save_memory(user_message: str, assistant_response: str):
    memory = load_memory()

    memory.append(
        {
            "user_message": user_message,
            "assistant_response": assistant_response
        }
    )

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)
