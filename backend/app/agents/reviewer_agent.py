from app.utils.llm import generate_response


def reviewer_agent(response: str):

    prompt = f"""
You are a Response Reviewer AI.

Improve the response below.

Rules:
- Improve clarity
- Improve grammar
- Improve formatting
- Keep the same meaning
- Return ONLY the final improved answer
- Do NOT explain your changes
- Do NOT add headings like "Review" or "Changes Made"

Response:

{response}
"""

    return generate_response(prompt)
