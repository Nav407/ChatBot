import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(user_message, context=""):
    prompt = f"""
    You are a helpful assistant for property management. Help tenants with their questions.
    Context: {context}
    Tenant: {user_message}
    Assistant:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response['choices'][0]['message']['content']