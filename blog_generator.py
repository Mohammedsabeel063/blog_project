import os
from datetime import datetime
import openai

# ✅ Load API key from environment
api_key = os.environ.get("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY not found in environment")
openai.api_key = api_key

def generate_blog(topic, tone='Informative', language='English', full=False):
    prompt = (
        f"Write a full blog post in {language} titled '{topic}' with introduction, body, and conclusion in a {tone} tone."
        if full else
        f"Write a {tone} paragraph in {language} about: {topic}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog-writing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    content = response.choices[0].message.content.strip()
    save_blog_to_file(topic, content)
    return content

def save_blog_to_file(topic, content):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    safe = "_".join(topic.lower().split())[:30]
    os.makedirs("blogs", exist_ok=True)
    fname = f"{safe}_{now}.txt"
    with open(os.path.join("blogs", fname), "w", encoding="utf-8") as f:
        f.write(content)
