from app.utils.llm import generate_response


def route_query(message: str):

    lower_message = message.lower()

    if "resume" in lower_message or "linkedin" in lower_message or "internship" in lower_message or "career" in lower_message:
        agent = "career_agent"

    elif "research" in lower_message or "explain" in lower_message or "summarize" in lower_message:
        agent = "research_agent"

    elif "remember" in lower_message or "my goal" in lower_message or "my name" in lower_message:
        agent = "personal_agent"

    else:
        agent = "general_agent"

    prompt = f"""
You are the {agent} in a Multi-Agent AI Career & Research Assistant.

User message:
{message}

Answer clearly and helpfully.
"""

    reply = generate_response(prompt)

    return {
        "agent": agent,
        "message": reply
    }
