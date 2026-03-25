expenses = []

while True:
    print("===Expenses===")
    print("1) Add expense")
    print("2) Show all")
    print("3) Show total")
    print("0) Exit")

    choice = int(input("Select option: "))

    if choice == 1:
        a = input("Name: ")
        b = int(input("Sum: "))
        expenses.append((a, b))
        print("Added!")
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses")
        else:
            i = 1
            for item in expenses:
                print(i, ".", item[0], "-", item[1])
                i += 1
    elif choice == 3:
        total = 0
        for item in expenses:
            total += item[1]
        print("Total:", total)
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Unknown option")






