#Error Handling
print("="*40)
print("Part 1: Basic Error Handling")
print("="*40)

try:
    number=int("hello")
except ValueError:
    print("Cant convert text to Number")
    

try:
    number=10/0
except ZeroDivisionError:
    print("Cant Divided by Zero")
    
try:
    student={"name":"Tayyab"}
    print(student["age"])
except KeyError:
    print("The Key doesnot exist in dictionary")



print("\n"+"="*40)
print("part2: FUll Error Handling")
print("="*40)

try:
    number=int(22)
    print("converting to number....")
except ValueError:
    print("Failed to Convert")
else:
    print(f"Success! Number is {number}")
finally:
    print("This always run no matter what!")
    


# API KEY ERROR HANDLING

print("\n" + "=" * 40)
print("PART 3: AI API ERROR HANDLING")
print("=" * 40)


import requests

def call_ai_api(api_key,prompt):
    try:
        if not api_key:
            raise ValueError("No API Key Provided")
        
        response = requests.get("https://httpbin.org/get", timeout=5)
        response.raise_for_status()
        
        data=response.json()
        print(f"API Call successfull")
        print(f"Prompt: {prompt}")
        print(f"Response{data}")
        return data
    except ValueError as e:
        print(f"Value Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection error : No Internet Connection")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error {e}")
    except Exception as e:
        print(f" Unexpected error as {e}")
    finally:
        print("API call attempt finished")


call_ai_api("tayyab-secret-123", "What is Python?")

print()

call_ai_api("","what is Python?")