#task 1
nums = [10, 5, 7, 3]

total = 0
for num in nums:
    total += num
print("Total:", total)

#task 2
scores = [3, 9, 1, 11, 4]

max_num = scores[0]
for s in scores:
    if s > max_num:
        max_num = s
print(max_num)

#task 3
ages = [12, 25, 17, 30, 14, 19]

for a in ages:
    if a >= 18:
        print(a)

#task 4
prices = [100, 250, 80]

new_prices = []

for p in prices:
    new_prices.append(p * 2)

print("Prices =", new_prices)