import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
response=os.getenv("groq_api_key")
print(response is not None)
client = OpenAI(
    api_key=response,
    base_url="https://api.groq.com/openai/v1"
)
print("client created successfully")
user_input=input("enter your question:")
result = client.responses.create(
    model="openai/gpt-oss-20b",
    input=user_input
)
print(result.output_text)