import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment variables.")

# Set the OpenAI API key globally
openai.api_key = api_key

def generate_blog(topic, tone='Informative', language='English', full=False):
    prompt = (
        f"Write a blog post in {language} titled '{topic}' with an introduction, body, and conclusion in a {tone} tone."
        if full else
        f"Write a short paragraph in {language} about '{topic}' in a {tone} tone."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful blog writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error generating blog: {e}"
