from google import genai
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Ask Gemini something
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain AI agents in simple words"
)

print(response.text)