import json

# ===== PART 1: PYTHON DICT TO JSON =====
print("=" * 40)
print("PART 1: DICT TO JSON")
print("=" * 40)

student = {
    "name": "Tayyab",
    "age": 22,
    "university": "COMSATS",
    "skills": ["Python", "React", "MongoDB"],
    "is_student": True,
    "gpa": 3.1
}

# convert dict to JSON string
json_string = json.dumps(student, indent=4)
print(json_string)
print(type(json_string))  # <class 'str'>


# ===== PART 2: JSON TO PYTHON DICT =====
print("\n" + "=" * 40)
print("PART 2: JSON TO DICT")
print("=" * 40)

json_data = '{"name": "Tayyab", "age": 22, "university": "COMSATS"}'

# convert JSON string to dict
python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict))  # <class 'dict'>
print("Name:", python_dict["name"])
print("Age:", python_dict["age"])


# ===== PART 3: SAVE JSON TO FILE =====
print("\n" + "=" * 40)
print("PART 3: SAVE JSON TO FILE")
print("=" * 40)

chat_history = {
    "user": "Tayyab",
    "messages": [
        {"role": "user", "content": "What is Python?"},
        {"role": "assistant", "content": "Python is a programming language!"},
        {"role": "user", "content": "What is AI?"},
        {"role": "assistant", "content": "AI is artificial intelligence!"}
    ]
}

# save to file
with open("chat_history.json", "w") as file:
    json.dump(chat_history, file, indent=4)

print("✅ Chat history saved to chat_history.json!")


# ===== PART 4: LOAD JSON FROM FILE =====
print("\n" + "=" * 40)
print("PART 4: LOAD JSON FROM FILE")
print("=" * 40)

with open("chat_history.json", "r") as file:
    loaded_history = json.load(file)

print(f"User: {loaded_history['user']}")
print("Messages:")
for message in loaded_history["messages"]:
    if message["role"] == "user":
        print(f"  👤 User: {message['content']}")
    else:
        print(f"  🤖 AI: {message['content']}")


# ===== PART 5: REAL WORLD - PARSE AI RESPONSE =====
print("\n" + "=" * 40)
print("PART 5: PARSE FAKE AI RESPONSE")
print("=" * 40)

fake_openai_response = '''
{
    "id": "chatcmpl-123",
    "model": "gpt-4",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Python is an amazing programming language!"
            }
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 25,
        "total_tokens": 35
    }
}
'''

# parse it
response = json.loads(fake_openai_response)

# extract the AI reply
ai_reply = response["choices"][0]["message"]["content"]
tokens_used = response["usage"]["total_tokens"]

print(f"🤖 AI Reply: {ai_reply}")
print(f"📊 Tokens Used: {tokens_used}")