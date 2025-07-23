import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is present
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not set in environment variables")

# Initialize OpenAI client using environment variable (SDK handles key automatically)
client = OpenAI()

def generate_blog(topic, tone='Informative', language='English', full=False):
    """
    Generates a blog based on user inputs.
    
    :param topic: Blog topic
    :param tone: Writing tone (e.g., 'Formal', 'Casual', etc.)
    :param language: Language to generate the blog in
    :param full: If True, generate full blog; else short paragraph
    :return: Generated blog content
    """
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
