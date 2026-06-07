from app.agents.career_agent import career_agent
from app.agents.research_agent import research_agent
from app.agents.personal_agent import personal_agent
from app.agents.reviewer_agent import reviewer_agent
from app.utils.llm import generate_response


def route_query(message: str):
    lower_message = message.lower()

    if (
        "review" in lower_message
        or "improve answer" in lower_message
        or "check answer" in lower_message
        or "evaluate" in lower_message
        or "feedback" in lower_message
        or "critique" in lower_message
    ):
        agent = "reviewer_agent"
        reply = reviewer_agent(message)

    elif (
        "resume" in lower_message
        or "linkedin" in lower_message
        or "internship" in lower_message
        or "career" in lower_message
    ):
        agent = "career_agent"
        reply = career_agent(message)

    elif (
        "research" in lower_message
        or "explain" in lower_message
        or "summarize" in lower_message
        or "what is rag" in lower_message
    ):
        agent = "research_agent"
        reply = research_agent(message)

    elif (
        "remember" in lower_message
        or "my goal" in lower_message
        or "my name" in lower_message
        or "what did i ask" in lower_message
    ):
        agent = "personal_agent"
        reply = personal_agent(message)

    else:
        agent = "general_agent"
        reply = generate_response(message)

    return {
        "agent": agent,
        "message": reply
    }
