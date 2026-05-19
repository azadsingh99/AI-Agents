from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def decide_route(user_question):

    prompt = f"""
    You are an AI routing system.

    Decide which information source is needed.

    Options:
    - company
    - internet
    - both

    Examples:

    Question:
    How many paid leaves do employees get?
    Answer:
    company

    Question:
    What are latest AI trends?
    Answer:
    internet

    Question:
    Based on latest AI trends, how can our company improve?
    Answer:
    both

    User Question:
    {user_question}

    Respond with only one word:
    company, internet, or both
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip().lower()