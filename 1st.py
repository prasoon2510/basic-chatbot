import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_keys = os.getenv("api_key")
obj = OpenAI(api_key=api_keys,  base_url="https://api.groq.com/openai/v1")
result = obj.responses.create(
    model = "openai/gpt-oss-20b",
    input= input("Enter the question:"))
print (result.output_text)
