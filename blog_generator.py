import os
from datetime import datetime
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

    blog_content = response.choices[0].message.content.strip()
    save_blog_to_file(topic, blog_content)
    return blog_content

def save_blog_to_file(topic, content):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    safe_topic = "_".join(topic.lower().split())[:30]
    filename = f"{safe_topic}_{now}.txt"
    os.makedirs("blogs", exist_ok=True)
    with open(os.path.join("blogs", filename), "w", encoding="utf-8") as f:
        f.write(content)
