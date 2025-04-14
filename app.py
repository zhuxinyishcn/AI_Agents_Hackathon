# Built for the Generative AI Hackathon #16
# Inbox Buddy - AI Email Assistant: Summarizes emails and generates smart replies using OpenAI GPT-3.5 and Gradio.
# Theresa

import gradio as gr
# import openai
import os
# from dotenv import load_dotenv

# Load API key from .env file
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate summary
def generate_summary(email_text):
    prompt = f"""
You are an AI assistant that summarizes emails.
Summarize the following email in 2-3 sentences:

Email:
\"\"\"{email_text}\"\"\"
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content'].strip()

# Function to generate reply
def generate_reply(email_text, tone):
    prompt = f"""
You are an AI writing assistant. Write a {tone} reply to the following email.
Keep it concise, polite, and relevant.

Email:
\"\"\"{email_text}\"\"\"

Reply:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Function called by Gradio
def inbox_buddy(email_text, tone):
    if not email_text:
        return "Please enter an email.", ""
    summary = generate_summary(email_text)
    reply = generate_reply(email_text, tone)
    return summary, reply

# Gradio UI
gr.Interface(
    fn=inbox_buddy,
    inputs=[
        gr.Textbox(label="📧 Paste Email Here", lines=10, placeholder="Paste the email text here..."),
        gr.Dropdown(["formal", "casual", "friendly", "urgent"], label="Reply Tone", value="formal")
    ],
    outputs=[
        gr.Textbox(label="📝 Summary"),
        gr.Textbox(label="✉️ Suggested Reply")
    ],
    title="📬 Inbox Buddy",
    description="An AI assistant that summarizes emails and suggests smart replies using GPT."
).launch()