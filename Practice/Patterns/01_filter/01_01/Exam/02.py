nums = [4, -3, 12, 0, 5, -8, 7, 15]

filtered = []
for n in nums:
    if n > 0:
        filtered.append(n)

result = []
for n in filtered:
    if n % 2 == 0:
        result.append(round(n / 2))

print("Task 2:", result)