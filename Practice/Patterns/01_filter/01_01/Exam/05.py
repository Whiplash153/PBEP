items = ["apple", "x", "banana", "test", "go", "orange", "tt", "cat", "tool"]

filtered = []
for item in items:
    if len(item) > 2 and item.count("t") >= 2:
        filtered.append(item)

result = []
for f in filtered:
    result.append({"Value": f, "Length": len(f)})

print(result)