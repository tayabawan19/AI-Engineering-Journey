class AIModel:
    def __init__(self,name,version):
        self.name=name
        self.version=version
    
    def describe(self):
        print (f"Model: {self.name},Version :{self.version}")
    
    def generate(self,prompt):
        return f"[{self.name}] Response to:'{prompt}'"
    
gpt=AIModel("GPT-4","4.0")
claude=AIModel("Claude",3.5)

gpt.describe()
claude.describe()

print(gpt.generate("What is Python?"))
print(claude.generate("Explain AI"))