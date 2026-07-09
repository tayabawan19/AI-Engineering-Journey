#if/else

score=85

if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
else:
    print("Grade : F")


#for loop
fruits=["apple","banana","mango"]

for fruit in fruits:
    print("Fruits: " ,fruit)
    

#while Loop
count=1
while count<=5:
    print("Count: ",count)
    count+=1


#Real World Example
#API key Response
messages=[
    {"role":"user","text":"Hello"},
    {"role":"assitant","text":"Hi these!"},
    {"role":"user","text":"How are you?"},
]

for message in messages:
    if message["role"]=="user":
        print(f"User:{message['text']}")
    else:
        print(f"AI:{message['text']}")