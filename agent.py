import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

def chat_with_ai(user_input):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load key
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content
