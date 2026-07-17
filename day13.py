from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()
client =Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(messages,label):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    print(f"\n{'='*50}")
    print(f"{label}")
    print('='*50)
    print(response.choices[0].message.content)

ask_ai(
    messages=[
        {"role": "user", "content": "Summarize what Python is."}
    ],
    label="ZERO-SHOT (no examples given)"
)

ask_ai(
    messages=[
        {"role": "user", "content": """Convert these to past tense:
"I run" -> "I ran"
"I eat" -> "I ate"
"I go" -> ?"""}
    ],
    label="FEW-SHOT (examples given first)"
)

ask_ai(
    messages=[
        {"role": "user", "content": "A store has 15 apples. They sell 6, then restock 10. How many apples now? Think step by step."}
    ],
    label="CHAIN-OF-THOUGHT (step by step reasoning)"
)

ask_ai(
    messages=[
        {"role": "system", "content": "You are a strict senior Python tutor. Only answer in under 2 sentences. Never use emojis."},
        {"role": "user", "content": "What is a variable?"}
    ],
    label="ROLE PROMPTING (system prompt controls behavior)"
)

ask_ai(
    messages=[
        {"role": "user", "content": "Tell me about dogs."}
    ],
    label="BAD PROMPT (vague)"
)

ask_ai(
    messages=[
        {"role": "user", "content": "Write a 3-sentence intro about Golden Retrievers for a pet care blog, focused on their temperament with families."}
    ],
    label="GOOD PROMPT (specific)"
)