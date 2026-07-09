#list
Skills=["React", "AI", "Node.js","MongoDB"]

print(Skills)
print(Skills[0]) #first item
print(Skills[-1]) #last item
print(len(Skills))

Skills.append("Java")
Skills.remove("React")
print(Skills)


for skill in Skills:
    print("I know ", skill)
    
#Dictionary

Student={
    "name":"Tayyab",
    "Age":22,
    "University":"COMSAT",
    "Semester":4 
}

print(Student["name"])
print(Student["Semester"])

Student["goal"]="AI Engineer"
print(Student)

for key, value in Student.items():
    print(f"{key}:{value}")

 
