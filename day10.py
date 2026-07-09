import json
import os
from datetime import datetime


class ChatManager:
    def __init__(self,username):
        self.username=username
        self.messages=[]
        self.filename=f"{username}_chat.json"
        self.load_history()
        
    def load_history(self):
        try:
            with open(self.filename,"r") as file:
                data=json.load(file)
                self.messages=data["messages"]
                print(f"Loaded {len(self.messages)} previous messages!")
        except FileNotFoundError:
            print("No previous chat history found. starting fresh")
        except Exception as e:
            print(f" Error Loading history: {e}")
    
    def save_history(self):
        try:
            data ={
                "username": self.username,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "messages": self.messages
            } 
            with open(self.filename,"w") as file:
                json.dump(data,file, indent=4)
                print("chart history saved!")
        except Exception as e:
            print(f"Error saving history : {e}")
    
    def add_message(self,role,content):
        message={
            "role":role,
            "content":content,
            "timestamp": datetime.now().strftime("%H:%M:%S")
            }
        self.messages.append(message)
    
    def fake_ai_response(self,user_input):
        responses ={
             "hello": "Hey Tayyab! How can I help you?",
            "what is python": "Python is an amazing programming language used in AI!",
            "what is ai": "AI is Artificial Intelligence — machines that can think!",
            "bye": "Goodbye! Chat history saved. See you next time!"
        }
        key=user_input.lower().strip()
        return responses.get(key,f"Interesting question! Your asked:'{user_input}'")
    
    def show_history(self):
        if not self.messages:
            print("📭 No messages yet!")
            return
        print("\n" + "=" * 40)
        print(" CHAT HISTORY")
        print("=" * 40)
        for msg in self.messages:
            if msg["role"] == "user":
                print(f"[{msg['timestamp']}]  You: {msg['content']}")
            else:
                print(f"[{msg['timestamp']}]  AI: {msg['content']}")
        print("=" * 40 + "\n")

def main():
    print("=" * 40)
    print("🤖 AI CHAT MANAGER")
    print("=" * 40)

    # create chat manager
    chat = ChatManager("Tayyab")

    print("\nCommands: 'history' = show history | 'quit' = exit\n")

    while True:
        try:
            user_input = input("👤 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                chat.save_history()
                print("👋 Goodbye!")
                break

            if user_input.lower() == "history":
                chat.show_history()
                continue

            # add user message
            chat.add_message("user", user_input)

            # get fake AI response
            ai_reply = chat.fake_ai_response(user_input)
            print(f"🤖 AI: {ai_reply}")

            # add AI message
            chat.add_message("assistant", ai_reply)

        except KeyboardInterrupt:
            chat.save_history()
            print("\n👋 Goodbye!")
            break

main()