from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)


def chat_mode():
    print("\nChat Mode (type 'back' to return)\n")

    while True:
        user = input("You: ")

        if user.lower() == "back":
            break

        response = llm.invoke(user)
        print("AI:", response.content)


def summary_mode():
    print("\nText Summarizer (type 'back' to return)\n")

    while True:
        text = input("Paste text: ")

        if text.lower() == "back":
            break

        prompt = "Summarize this in simple bullet points:\n\n" + text
        response = llm.invoke(prompt)

        print("\nSummary:\n", response.content)


def main_menu():
    while True:
        print("\n=================================")
        print("🤖 AI APP")
        print("=================================")
        print("1. Chat with AI")
        print("2. Summarize text")
        print("3. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            chat_mode()

        elif choice == "2":
            summary_mode()

        elif choice == "3":
            print("Bye! 👋")
            break

        else:
            print("Invalid Option ❌ Try again.")


if __name__ == "__main__":
    main_menu()
