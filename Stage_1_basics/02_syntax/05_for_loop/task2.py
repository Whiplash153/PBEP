words = ["apple", "hi", "banana", "cat", "watermelon"]
count = 0

for w in words:
    if len(w) > 3:
        count += 1
        print("Word:", w)
