# LifeChart

AI-powered BaZi (八字) destiny analysis app. Enter your birth date and time to receive a personalized reading of your Four Pillars, Five Elements, personality traits, and 2026 fortune — in English or Chinese.

Built with Claude API, FastAPI, and vanilla JavaScript.

---

## Features

- Bilingual support — English and Chinese
- Mobile-first card layout
- Structured AI responses via Claude Sonnet
- Clean dark UI

---

## Tech Stack

- **AI**: Anthropic Claude API
- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML, CSS, Vanilla JavaScript

---

## Quick Start

Clone the repo and install dependencies:

```bash
pip install anthropic fastapi uvicorn
```

Set your Anthropic API key:

```bash
# Mac/Linux
export ANTHROPIC_API_KEY="your-key-here"

# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-key-here"
```

Run the app:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`

---

## Roadmap

- Deploy to Railway
- Add Zi Wei Dou Shu analysis
- Add Tarot integration
- User accounts and reading history

---

## Author

Jing You — Data Engineer & Analytics Engineer  
[LinkedIn](https://linkedin.com/in/jingyou84) · [GitHub](https://github.com/JingYou-data)