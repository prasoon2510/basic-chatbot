
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

# Connect OpenAI Python client to Groq
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer clearly and politely."
    }
]
print(messages)
print("=" * 50)
print("       WELCOME TO MY TERMINAL AI CHATBOT")
print("=" * 50)
print("Type your question to chat with AI.")
print("Type 'exit' to stop the chatbot.")
print("=" * 50)

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("\nAI: Goodbye! Have a nice day.")
        break

    if not user_input:
        print("Please enter a question.")
        continue

    # Add user message to conversation
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Send request to Groq AI
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.7
        )

        # Get AI response
        ai_response = response.choices[0].message.content

        # Display AI response
        print("\nAI:", ai_response)

        # Store AI response for conversation memory
        messages.append({
            "role": "assistant",
            "content": ai_response
        })

    except Exception as error:
        print("\nError:", error)
        messages.pop()

