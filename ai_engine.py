import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def chat(user_input):
    try:
        return model.generate_content(user_input).text
    except Exception as e:
        return f"Error: {str(e)}"

def summarize(text):
    try:
        prompt = "Summarize this in simple bullet points:\n\n" + text
        return model.generate_content(prompt).text
    except Exception as e:
        return f"Error: {str(e)}"
