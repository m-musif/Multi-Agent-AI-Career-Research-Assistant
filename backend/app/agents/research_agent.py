from app.utils.llm import generate_response


def research_agent(message: str):

    prompt = f"""
You are a Research Assistant AI.

Provide:

- Detailed explanations
- Summaries
- Technical research
- Learning guidance

User:
{message}
"""

    return generate_response(prompt)
