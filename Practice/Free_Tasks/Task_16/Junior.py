a = input("Type a: ")
b = input("Type b: ")

try:
    result = int(a) / int(b)
    print("Result:", result)
except:
    print("Something went wrong!")

print("Operation finished")