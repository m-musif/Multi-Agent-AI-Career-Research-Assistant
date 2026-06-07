from app.utils.llm import generate_response


def personal_agent(message: str):

    prompt = f"""
You are a Personal Assistant AI.

Help with:

- Goals
- Productivity
- Planning
- Personal guidance

User:
{message}
"""

    return generate_response(prompt)
