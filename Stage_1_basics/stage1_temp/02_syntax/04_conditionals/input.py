login = input("Enter login: ")

if login == "admin":
    print("Welcome admin")
else:
    age = int(input("Enter your age: "))
    if login == "vip" and age >= 16:
        print("Welcome VIP")
    elif age >= 18:
        print("Access granted")
    else:
        print("Access denied")
