# LifeChart 🔮
### AI-Powered BaZi Destiny Analysis | AI八字命理分析

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com)
[![Claude API](https://img.shields.io/badge/Claude-Sonnet-orange)](https://anthropic.com)

LifeChart is a full-stack AI application that generates personalized BaZi (八字) destiny readings using the Claude API. Users enter their birth date and time to receive a structured analysis of their Four Pillars, Five Elements, personality traits, and 2026 fortune — in English or Chinese.

---

## ✨ Features

- 🔮 **AI-Powered Readings** — Claude Sonnet generates detailed BaZi analysis
- 🌏 **Bilingual** — Full English / Chinese language toggle
- 📱 **Mobile-First** — Card-based UI optimized for phone reading
- ⚡ **Fast** — FastAPI backend with structured JSON responses
- 🎨 **Beautiful UI** — Dark theme with gold accents

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| AI | Anthropic Claude API (claude-sonnet-4-5) |
| Backend | Python · FastAPI · Uvicorn |
| Frontend | HTML · CSS · Vanilla JavaScript |
| Data Format | Structured JSON responses |

---

## 🚀 Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/JingYou-data/lifechart.git
cd lifechart
```

**2. Install dependencies**
```bash
pip install anthropic fastapi uvicorn
```

**3. Set your API key**
```bash
# Mac/Linux
export ANTHROPIC_API_KEY="your-key-here"

# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-key-here"
```

**4. Run**
```bash
uvicorn main:app --reload
```

**5. Open** `http://127.0.0.1:8000`

---

## 📸 Screenshots

*Coming soon*

---

## 🔭 Roadmap

- [ ] Deploy to Railway
- [ ] Add Zi Wei Dou Shu (紫微斗数) analysis
- [ ] Add Tarot integration
- [ ] User accounts and reading history
- [ ] Payment integration

---

## 👩‍💻 Author

**Jing You** — Data Engineer & Analytics Engineer  
[LinkedIn](https://linkedin.com/in/jingyou84) · [GitHub](https://github.com/JingYou-data)