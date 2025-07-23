import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set API key globally for openai package
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog(topic, tone='Informative', language='English', full=False):
    prompt = (
        f"Write a blog post in {language} titled '{topic}' with introduction, body, and conclusion in a {tone} tone."
        if full else
        f"Write a short paragraph in {language} about '{topic}' in a {tone} tone."
    )

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
