nums = [10, -4, 3, 22, 0, 5, 14, -1, 7, 18]

filtered = []
for n in nums:
    if n > 5 and n % 2 != 0:
        filtered.append(n)

result = []
for f in filtered:
    result.append(f"value: {f}")

print("Task 4:", result)