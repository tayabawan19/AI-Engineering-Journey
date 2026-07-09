
#basic Function
def greet(name):
    print(f"Hello {name}")

greet("Tayyab")
greet("Hamza")


def add(a,b):
    return a+b

result=add(5,2)
result2=add(12,3)

print("Sum =", result)
print("Sum2 ",result2)


#function with default value
def introduce(name,role="AI Engineer"):
    return f"My Name is {name} and I am a {role}"

print(introduce("Tayyab"))
print(introduce("Tayyab","Student"))

#Processing API Response 
def get_response_text(response):
    return response["choices"][0]["text"]


fake_response={
    "choices":[
        {"text":"Hello I am an AI Assistant"}
    ]
}
print(get_response_text(fake_response))