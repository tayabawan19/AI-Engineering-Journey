import json
import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))


class ChatManager:
    def __init__(self,username):
        self.username=username
        self.messages=[]
        self.filename=f"{username}_chat.json"
        self.loadhistory()
        
    def loadhistory(self):
        
        try:
            with open(self.filename,"r") as file:
                data=json.load(file)
                self.messages=data["messages"]
                print(f"loaded {len(self.messages)} prevous messages!")
        except FileNotFoundError:
            print("No previous chat history found ")
        except Exception as e:
            print("Error loading history {e}")        
            
    def save_history(self):
        try:
            data={
                "username":self.username,
                "last_updated":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "messages":self.messages
            }
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            print(" Chat history saved!")
        except Exception as e:
            print(f" Error saving history: {e}")
    
    def add_message(self,role,content):
        self.messages.append({
            "role":role,
            "content":content,
            "timestamp":datetime.now().strftime("%H:%M:%S")
        })
    
    
    def get_ai_response(self,user_input):
        self.add_message("user",user_input)
        
        api_messages=[
            {"role":m["role"],"content":m["content"]}
             for m in self.messages
        ]
        
        try:
            response=client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages
            )
            
            api_reply=response.choices[0].message.content 
            self.add_message("AI:",api_reply)
            return api_reply
        except Exception as e:
            error_msg = f" Error getting AI response: {e}"
            print(error_msg)
            return "Sorry, something went wrong!"

    def show_history(self):
        if not self.messages:
            print(" No messages yet!")
            return
        print("\n" + "=" * 40)
        print(" CHAT HISTORY")
        print("=" * 40)
        for msg in self.messages:
            emoji = " You" if msg["role"] == "user" else "🤖 AI"
            print(f"[{msg['timestamp']}] {emoji}: {msg['content']}")
        print("=" * 40 + "\n")


def main():
    print("=" * 40)
    print(" REAL AI CHATBOT (with memory)")
    print("=" * 40)

    chat = ChatManager("Tayyab")
    print("\nCommands: 'history' = show history | 'quit' = exit\n")

    while True:
        try:
            user_input = input(" You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                chat.save_history()
                print(" Goodbye!")
                break

            if user_input.lower() == "history":
                chat.show_history()
                continue

            ai_reply = chat.get_ai_response(user_input)
            print(f" AI: {ai_reply}")

        except KeyboardInterrupt:
            chat.save_history()
            print("\n Goodbye!")
            break

main()