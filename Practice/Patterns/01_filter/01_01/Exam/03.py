words = ["hello", "hi", "python", "a", "filter", "cat", "super"]

filtered = []
for w in words:
    if "t" in w:
        filtered.append(w)

result = []
for f in filtered:
    result.append(len(f))

print("Task 3:", result)