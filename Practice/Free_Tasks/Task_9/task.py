reviews = {
    "Anna": 5,
    "Sergey": 3,
    "Masha": 4,
    "Oleg": 5,
    "Ivan": 2
}

got_5 = [name for name, mark in reviews.items() if mark == 5]
print("Got 5:", got_5)

total = 0
for name, mark in reviews.items():
    total += mark

print("Average:", round(total / len(reviews)))