import os
from flask import Flask, request, render_template, session, send_from_directory
from posthog import Posthog
from blog_generator import generate_blog
from dotenv import load_dotenv

load_dotenv()  # This loads .env locally, does nothing on Render
openai.api_key = os.environ['API_KEY']

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Initialize PostHog
ph = Posthog(os.getenv("POSTHOG_API_KEY"), host=os.getenv("POSTHOG_HOST"))

# Optional manual test event
@app.route('/test_event')
def test_event():
    ph.capture(
        distinct_id="manual_test_user",
        event="generate_blog",
        properties={"topic": "Test Topic", "full_blog": "This is a test blog content"}
    )
    return "✅ Test event sent!"

# Generate unique session ID
@app.before_request
def set_session_id():
    if "session_id" not in session:
        session["session_id"] = os.urandom(16).hex()

# Home route — blog generation and event capture
@app.route('/', methods=['GET', 'POST'])
def home():
    blog = ''
    if request.method == 'POST':
        topic = request.form['topic']
        tone = request.form.get('tone', 'Informative')
        language = request.form.get('language', 'English')
        full = 'full' in request.form

        blog = generate_blog(topic, tone, language, full)

        # Capture event with full blog content
        ph.capture(
            distinct_id=session["session_id"],
            event="generate_blog",
            properties={
                "topic": topic,
                "tone": tone,
                "language": language,
                "full_blog": blog
            }
        )

    return render_template('index.html', blog=blog)

# Blog history route
@app.route('/history')
def history():
    files = sorted(os.listdir('blogs'), reverse=True)
    entries = [
        {
            'filename': fn,
            'topic': fn.rsplit('_', 1)[0].replace('_', ' '),
            'timestamp': fn.rsplit('_', 1)[1].replace('.txt', '')
        }
        for fn in files if fn.endswith('.txt')
    ]
    return render_template('history.html', entries=entries)

# Download blog file
@app.route('/blogs/<filename>')
def download_blog(filename):
    return send_from_directory('blogs', filename, as_attachment=True)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
