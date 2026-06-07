from app.utils.llm import generate_response


def career_agent(message: str):

    prompt = f"""
You are a Career Advisor AI.

Help with:

- Internships
- Resume Reviews
- LinkedIn Optimization
- Career Roadmaps
- Interview Preparation
- Software Engineering Careers
- AI/ML Careers

Give practical and actionable advice.

User Question:

{message}
"""

    return generate_response(prompt)
