# writing a file
with open("data.txt","w") as file:
    file.write("Hello Tayyab:\n")
    file.write("This is your first file.\n")
    file.write("AI Engineering is awesome!\n")

print("File written successfully!")

#reading a fike
with open("data.txt","r") as file:
    content=file.read()
    print(content)

#reading line by line
with open("data.txt","r") as file:
    for line in file:
        print("Lines: ",line.strip())
    
#Save AI Conversation history to a file

messages=[
    {"role":"user","text":"hello"},
    {"role":"assitant","text":"Hi there!"},
    {"role":"user","text":"How are You?"},
]

with open("chat_history.txt","w") as file:
    for message in messages:
        if message["role"]=="user":
            file.write(f"User: {message['text']}\n")
        else:
            file.write(f"AI: {message['text']}\n")

print("chat history saved!")


#read it back
with open("chat_history.txt","r") as file:
    print(file.read())