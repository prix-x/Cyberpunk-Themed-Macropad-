from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def chat(user_input):
    return llm.invoke(user_input).content

def summarize(text):
    prompt = "Summarize this in simple bullet points:\n\n" + text
    return llm.invoke(prompt).content
