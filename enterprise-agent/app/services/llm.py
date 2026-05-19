from google import genai
from dotenv import load_dotenv
from services.web_search import search_web
from services.router import decide_route
import os

# Load env variables
load_dotenv()

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_agent(user_question, chat_history):

    # Decide route
    route = decide_route(user_question)

    company_data = ""
    internet_data = ""

    # Get company data if needed
    if route in ["company", "both"]:
        with open("data/company_data.txt", "r", encoding="utf-8") as file:
            company_data = file.read()

    # Get internet data if needed
    if route in ["internet", "both"]:
        internet_data = search_web(user_question)

    # Convert memory into text
    memory_text = ""

    for chat in chat_history:
        memory_text += f"""
User: {chat["user"]}
Assistant: {chat["assistant"]}
"""

    # Final prompt
    prompt = f"""
    You are an enterprise AI assistant.

    Conversation Memory:
    {memory_text}

    Routing Decision:
    {route}

    COMPANY DATA:
    {company_data}

    INTERNET DATA:
    {internet_data}

    USER QUESTION:
    {user_question}

    Rules:
    - Remember previous conversation
    - Use company data for company questions
    - Use internet for current/latest info
    - Combine both when useful
    - Be professional and concise
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return f"\n[Route Used: {route}]\n\n{response.text}"