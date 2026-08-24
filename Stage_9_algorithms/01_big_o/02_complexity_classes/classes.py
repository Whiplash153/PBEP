# O(1) — Количество элементов не влияет на количество операций

numbers = [10, 20, 30, 40, 50]

first_number = numbers[0]
print(first_number)

# O(n) — Количество операций растет с количеством элементов

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 40:
        print(number)

# O(n²) — каждый элемент сравнивается с каждым элементом

numbers = [10, 20, 30, 40, 50]

for first_number in numbers:
    for second_number in numbers:
        print(first_number, second_number)

# O(log n) — на каждом шаге уменьшаем область поиска в два раза

numbers = [1, 3, 5, 7, 9, 11, 13, 15]

target = 13

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print(target)
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1