import os
from datetime import datetime
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_blog(topic, tone='Informative', language='English', full=False):
    prompt = (f"Write a full blog post in {language} titled '{topic}' with introduction, body, conclusion, in a {tone} tone."
              if full else f"Write a {tone} paragraph in {language} about: {topic}")
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a helpful blog-writing assistant."},
                  {"role":"user","content":prompt}],
        temperature=0.3, max_tokens=800
    )
    content = resp.choices[0].message.content.strip()
    save_blog_to_file(topic, content)
    return content

def save_blog_to_file(topic, content):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    safe = "_".join(topic.lower().split())[:30]
    os.makedirs("blogs", exist_ok=True)
    fname = f"{safe}_{now}.txt"
    with open(os.path.join("blogs", fname), "w", encoding="utf-8") as f:
        f.write(content)
