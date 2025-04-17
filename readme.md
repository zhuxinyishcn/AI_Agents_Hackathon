# 📬 Inbox Buddy

**Inbox Buddy** is your personal AI-powered email assistant, built during the Generative AI Hackathon #16 - AI Agents. It helps you summarize lengthy emails and generate smart, tone-adjusted replies — instantly!

---

## 🧠 Why Inbox Buddy?

### 🚨 The Problem
Email overload is real. Professionals and students spend too much time reading and replying to emails, often just trying to get to the main point or craft a polite response.

### 💡 The Solution
Inbox Buddy is a lightweight AI tool that:
- ✂️ Summarizes long emails into 2–3 digestible sentences.
- ✍️ Writes smart, customizable replies in different tones (formal, casual, friendly, urgent).

> Just paste your email, pick a tone, and get instant help — all from your browser!

---

## 🔧 Tech Stack

| Component      | Tech |
|----------------|------|
| LLM            | OpenAI GPT-3.5-turbo |
| UI             | Gradio |
| Language       | Python 3.11+ |
| Env Management | `python-dotenv` |

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone git@github.com:zhuxinyishcn/AI_Agents_Hackathon.git
cd AI_Agents_Hackathon
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your .env file with your OpenAI API key:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app
```bash
python app.py
```
```markdown
---

## 📄 Project Proposal
Title: Inbox Buddy – AI-Powered Email Assistant

### Problem
Reading and responding to emails consumes valuable time. People need a way to quickly get the gist of long emails and reply efficiently without sacrificing politeness or clarity.

### Solution
Inbox Buddy uses OpenAI’s GPT-3.5-turbo model to:
- Generate concise summaries of any email
- Craft smart replies tailored to a selected tone
It’s built for professionals, students, and anyone who deals with email overload daily.

### What It Does
- Takes raw email text
- Produces a summary and reply suggestion
- Offers reply tone options (formal, casual, friendly, urgent)

### Future Features
- Gmail API integration
- Save and reuse replies
- Tone detection from input email
- Deploy as Chrome Extension

## Team 
- Theresa Hsu
- Xinyi Zhu