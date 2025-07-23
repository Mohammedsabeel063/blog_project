# 📝 AI Blog Generator Web App

A Flask-based AI-powered blogging assistant that helps users create well-structured blog posts instantly by entering a **topic**, **tone**, and **language**. It uses **OpenAI GPT-3.5** for content generation, integrates **PostHog** for analytics, and allows users to download their generated blogs for future use.

🚀 **Live Demo:**  
👉 [https://blog-project-hb0o.onrender.com/](https://blog-project-hb0o.onrender.com/)

---

## 🔍 Overview

Writing quality blog content can be time-consuming. This project streamlines the process using AI to help users create structured, engaging blog posts in seconds. Just enter a topic, choose your tone and language, and click generate — your blog is ready!

The app supports content history, session tracking via PostHog, and downloadable `.txt` versions of every post.

---

## ✨ Features

- 🧠 Generate AI-written blogs based on:
  - Topic  
  - Tone (Informative, Casual, etc.)  
  - Language (English, Hindi, etc.)  
  - Full-length or short paragraph format  

- 💾 Blogs are saved locally in a `blogs/` directory
- 📜 View history and download previous blog posts
- 📈 User interactions tracked via **PostHog**
- 🔒 Anonymous session tracking (no login required)
- ⚙️ Secure API key handling using `.env`
- 🌐 Clean UI with Jinja2 templating

---

## 🧰 Tech Stack

- **Python 3.7+**
- **Flask** (Web Framework)
- **OpenAI GPT-3.5** (Blog generation)
- **PostHog** (Event tracking & analytics)
- **Jinja2** (Templates)
- **HTML/CSS** (Bootstrap optional)
- **dotenv** (Environment config)

---

## 🧠 Powered by OpenAI

The app uses OpenAI's `gpt-3.5-turbo` model to generate blog content. The logic is inside `blog_generator.py`, which takes user input and dynamically builds a prompt for the AI.

### Example prompt:
