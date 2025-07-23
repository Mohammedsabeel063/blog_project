# 📝 AI Blog Generator Web App

A Flask-based web application that allows users to generate blog posts using AI based on a given **topic**, **tone**, and **language**. The app also tracks usage with **PostHog**, stores blog files locally, and provides a history view for downloads.

---

## 🔍 Overview

Writing high-quality blog content consistently can be time-consuming. This project automates the blog writing process using AI, making it easier for users to generate informative, engaging, and well-structured blog posts within seconds.

The app also supports analytics tracking using PostHog and allows users to download previously generated blogs from a history page.

---

## 🚀 Features

- ✏️ Generate blog posts based on:
  - Topic
  - Tone (e.g. Informative, Casual, Formal)
  - Language (e.g. English, others)
  - Full/short blog toggle
- 📊 Tracks user sessions and events with **PostHog**
- 💾 Saves generated blogs as `.txt` files in a local `blogs/` folder
- 📁 Displays blog history with download links
- 🔒 Session-based user identification (no login required)
- 🌐 Built with clean Flask routing and Jinja2 templates

---

## 🧰 Technologies Used

- **Python**
- **Flask**
- **PostHog** (event tracking)
- **dotenv** (for environment variables)
- **Jinja2** (template engine)
- **HTML/CSS (Bootstrap or custom styling)**

---

## ⚙️ Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package manager)
- Optional: virtual environment setup (`venv`, `virtualenv`, or `conda`)

### 1. Clone the Repository

```bash
git clone https://github.com/Mohammedsabeel063/blog_project.git
cd blog_project
