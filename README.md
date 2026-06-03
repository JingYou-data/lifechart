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

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your-key-here
```

Run the app — **use PowerShell on Windows** (not Git Bash, to avoid SSL issues):

```powershell
python -m uvicorn main:app --port 8000
```

Open `http://localhost:8000`

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