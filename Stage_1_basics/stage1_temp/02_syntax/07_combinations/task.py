while True:
    print("===MENU===")
    print("1) Add two numbers")
    print("2) Check password")
    print("0) Exit")

    choice = input("Select option: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)
    elif choice == "2":
        password = input("Enter password: ")
        if password == "secret":
            print("Access granted")
        else:
            print("Wrong password")
    elif choice == "0":
        print("Exit selected")
        break
    else:
        print("Unknown option")

