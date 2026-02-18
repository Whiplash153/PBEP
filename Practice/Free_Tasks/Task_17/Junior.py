def safe_divide():
    a = input("Number 1: ")
    b = input("Number 2: ")

    try:
        a = int(a)
        b = int(b)
        result = a / b
        print(result)
    except:
        print("Error!")