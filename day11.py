from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

client =Groq(api_key=api_key)

print("="*40)
print("Real AI Model")
print("="*40)

response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # free, fast, powerful
    messages=[
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ]
)

ai_reply=response.choices[0].message.content 
print("AI says: ",ai_reply)

print("\n Tokens used:",response.usage.total_tokens)
