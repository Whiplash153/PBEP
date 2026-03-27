password = ""

while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password")

print("Access granted")