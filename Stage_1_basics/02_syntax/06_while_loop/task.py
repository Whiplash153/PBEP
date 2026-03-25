number = 1
total = 0

while number != 0:
    number = int(input("Enter number: "))
    total += number
    if number == 0:
        break

print("Sum:", total)
