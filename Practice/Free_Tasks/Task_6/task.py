expenses = ["1200", "550", "abc", "", "300", "200x", "400"]

total = 0

for e in expenses:
    try:
        total = total + int(e)
    except ValueError:
        continue

print("Total:", total)