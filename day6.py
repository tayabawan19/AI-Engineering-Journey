import requests
from dotenv import load_dotenv
import os

#calling an API
print("="*40)
print("Part 1: API Request")
print("="*40)

response=requests.get("https://jsonplaceholder.typicode.com/todos/1")

print("Status Code:",response.status_code)
print("Raw Response:", response.json())

#Extract Specific Feilds
data=response.json()
print("ID:",data["id"])
print("Title:",data["title"])
print("Completed:",data["completed"])

#ENV File
print("\n"+"="*40)
print("Part 2: API key from .ENV")

load_dotenv()
api_key=os.getenv("MY_API_KEY")
print("My API Key: ",api_key)

print("\n" + "=" * 40)
print("PART 3: SIMULATE AI API CALL")
print("=" * 40)

def call_ai_api(prompt,api_key):
    if api_key is None:
        print("Error 401: NO API Key found")
        return None

    print(f"API key Found :{api_key}")
    print(f"Sending Prompt:{prompt}")
    print(f"AI Response: 'Hello Tayyab Here is your answer!'")

call_ai_api("what is python?",api_key)