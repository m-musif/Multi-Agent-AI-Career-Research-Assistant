from app.utils.llm import generate_response


def research_agent(message: str):

    prompt = f"""
You are a Research Assistant AI.

Your job:

- Explain concepts
- Summarize topics
- Compare technologies
- Analyze trends
- Provide educational answers

Always provide:

1. Clear explanation
2. Key points
3. Examples when useful
4. Short conclusion

User Question:

{message}
"""

    return generate_response(prompt)
