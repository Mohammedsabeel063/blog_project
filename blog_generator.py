import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment variables")

client = OpenAI(api_key=api_key)

def generate_blog(topic, tone='Informative', language='English', full=False):
    prompt = (
        f"Write a blog post in {language} titled '{topic}' with introduction, body, and conclusion in a {tone} tone."
        if full else
        f"Write a short paragraph in {language} about '{topic}' in a {tone} tone."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog writing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content.strip()
