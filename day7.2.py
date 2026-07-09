
class AIModel:
    def __init__(self, name, version, company):
        self.name = name
        self.version = version
        self.company = company
        self.conversation_history = []  # empty list to store chat

    def describe(self):
        print(f"Model: {self.name} v{self.version} by {self.company}")

    def chat(self, prompt):
        # add user message to history
        self.conversation_history.append({
            "role": "user",
            "text": prompt
        })

        # fake AI response
        response = f"[{self.name}] answered: '{prompt}'"

        # add AI response to history
        self.conversation_history.append({
            "role": "assistant",
            "text": response
        })

        return response

    def show_history(self):
        print(f"\n📜 Conversation History for {self.name}:")
        for message in self.conversation_history:
            if message["role"] == "user":
                print(f"  👤 User: {message['text']}")
            else:
                print(f"  🤖 AI: {message['text']}")


# ===== CREATING OBJECTS =====
gpt = AIModel("GPT-4", "4.0", "OpenAI")
claude = AIModel("Claude", "3.5", "Anthropic")

# describe them
gpt.describe()
claude.describe()

# chat with gpt
print("\n", gpt.chat("What is Python?"))
print(gpt.chat("What is AI Engineering?"))

# chat with claude
print("\n", claude.chat("What is Machine Learning?"))

# show histories
gpt.show_history()
claude.show_history()