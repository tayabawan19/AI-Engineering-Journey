import json
import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

# ===== SETUP =====
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ===== PERSONAL AI ASSISTANT CLASS =====
class ChatManager:
    def __init__(self, username):
        self.username = username
        self.messages = []
        self.mode = "casual"  # default mode
        self.filename = f"{username}_assistant.json"
        self.load_history()

    def load_history(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.messages = data["messages"]
                self.mode = data.get("mode", "casual")
                print(f"Loaded {len(self.messages)} previous messages! (mode: {self.mode})")
        except FileNotFoundError:
            print(" No previous history found. Starting fresh!")
        except Exception as e:
            print(f" Error loading history: {e}")

    def save_history(self):
        try:
            data = {
                "username": self.username,
                "mode": self.mode,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "messages": self.messages
            }
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            print(" Saved!")
        except Exception as e:
            print(f" Error saving history: {e}")

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

    def get_system_prompt(self):
        prompts = {
            "tutor": "You are a patient, encouraging tutor. Explain concepts simply using real-world examples. Keep answers under 4 sentences unless asked for more detail.",
            "casual": "You are a friendly, casual assistant. Talk like a supportive friend, keep it relaxed and short.",
            "code": "You are a strict senior software engineer. Only give clean, correct code with minimal explanation unless asked to elaborate."
        }
        return prompts.get(self.mode, prompts["casual"])

    def set_mode(self, new_mode):
        valid_modes = ["tutor", "casual", "code"]
        if new_mode in valid_modes:
            self.mode = new_mode
            print(f" Mode switched to: {new_mode}")
        else:
            print(f" Invalid mode. Choose from: {', '.join(valid_modes)}")

    def get_ai_response(self, user_input):
        self.add_message("user", user_input)

        # system prompt goes first, then full clean history
        api_messages = [{"role": "system", "content": self.get_system_prompt()}]
        api_messages += [
            {"role": m["role"], "content": m["content"]}
            for m in self.messages
        ]

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages
            )
            ai_reply = response.choices[0].message.content
            self.add_message("assistant", ai_reply)
            return ai_reply

        except Exception as e:
            print(f" Error getting AI response: {e}")
            return "Sorry, something went wrong on my end!"

    def show_history(self):
        if not self.messages:
            print(" No messages yet!")
            return
        print("\n" + "=" * 40)
        print(f"CHAT HISTORY (mode: {self.mode})")
        print("=" * 40)
        for msg in self.messages:
            emoji = " You" if msg["role"] == "user" else " AI"
            print(f"[{msg['timestamp']}] {emoji}: {msg['content']}")
        print("=" * 40 + "\n")


# ===== MAIN PROGRAM =====
def choose_mode():
    print("\nChoose a mode:")
    print("1. tutor  → patient teacher, simple explanations")
    print("2. casual → friendly, relaxed chat")
    print("3. code   → strict senior dev, code-only answers")

    mode_map = {"1": "tutor", "2": "casual", "3": "code"}
    choice = input("Enter 1, 2, or 3: ").strip()
    return mode_map.get(choice, "casual")


def main():
    print("=" * 40)
    print(" PERSONAL AI ASSISTANT")
    print("=" * 40)

    chat = ChatManager("Tayyab")

    # only ask for mode if it's a brand new session
    if not chat.messages:
        chat.mode = choose_mode()

    print(f"\n Assistant ready in '{chat.mode}' mode.")
    print("Commands: 'mode' = switch mode | 'history' = show history | 'quit' = exit\n")

    while True:
        try:
            user_input = input("👤 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                chat.save_history()
                print(" Goodbye!")
                break

            if user_input.lower() == "history":
                chat.show_history()
                continue

            if user_input.lower() == "mode":
                new_mode = choose_mode()
                chat.set_mode(new_mode)
                continue

            ai_reply = chat.get_ai_response(user_input)
            print(f" AI: {ai_reply}")

        except KeyboardInterrupt:
            chat.save_history()
            print("\n👋 Goodbye!")
            break


main()