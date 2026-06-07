from app.utils.llm import generate_response


def career_agent(message: str):

    prompt = f"""
You are a Career Advisor AI.

Help with:

- Internships
- Resume reviews
- LinkedIn optimization
- Career roadmaps
- Interview preparation

User:
{message}
"""

    return generate_response(prompt)
