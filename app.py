import os
from flask import Flask, request, render_template, session, send_from_directory
from dotenv import load_dotenv
from posthog import Posthog
from blog_generator import generate_blog

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)

# Initialize PostHog
ph = Posthog(
    project_api_key=os.getenv("POSTHOG_API_KEY"),
    host=os.getenv("POSTHOG_HOST", "https://app.posthog.com")
)

# Ensure blogs directory exists
os.makedirs("blogs", exist_ok=True)

@app.before_request
def set_session_id():
    if "session_id" not in session:
        session["session_id"] = os.urandom(16).hex()

@app.route('/', methods=['GET', 'POST'])
def home():
    blog = ''
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        tone = request.form.get('tone', 'Informative')
        language = request.form.get('language', 'English')
        full = bool(request.form.get('full'))

        if topic:
            blog = generate_blog(topic, tone, language, full)

            # Track with PostHog
            ph.capture(
                distinct_id=session["session_id"],
                event="generate_blog",
                properties={
                    "topic": topic,
                    "tone": tone,
                    "language": language,
                    "full": full
                }
            )

    return render_template('index.html', blog=blog)

@app.route('/history')
def history():
    files = sorted(os.listdir('blogs'), reverse=True)
    entries = []
    for fn in files:
        if fn.endswith('.txt'):
            parts = fn.rsplit('_', 1)
            if len(parts) == 2:
                topic = parts[0].replace('_', ' ')
                timestamp = parts[1].replace('.txt', '')
                entries.append({'filename': fn, 'topic': topic, 'timestamp': timestamp})
    return render_template('history.html', entries=entries)

@app.route('/blogs/<filename>')
def download_blog(filename):
    return send_from_directory('blogs', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
