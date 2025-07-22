import tkinter as tk
from blog_generator import generate_blog

def generate():
    topic = topic_entry.get()
    tone = tone_entry.get()
    lang = lang_entry.get()
    blog_text.delete(1.0, tk.END)
    result = generate_blog(topic, tone, lang)
    blog_text.insert(tk.END, result)

root = tk.Tk()
root.title("Blog Generator")

tk.Label(root, text="Topic").pack()
topic_entry = tk.Entry(root)
topic_entry.pack()

tk.Label(root, text="Tone").pack()
tone_entry = tk.Entry(root)
tone_entry.insert(0, "friendly")
tone_entry.pack()

tk.Label(root, text="Language").pack()
lang_entry = tk.Entry(root)
lang_entry.insert(0, "English")
lang_entry.pack()

tk.Button(root, text="Generate", command=generate).pack()

blog_text = tk.Text(root, wrap='word', height=10, width=60)
blog_text.pack()

root.mainloop()
