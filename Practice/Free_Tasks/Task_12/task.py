orders = [
    ("croissant", 120),
    ("baguette", 80),
    ("eclair", 150),
]

def orders_sum(amount):
    if not amount:
        return None

    total = 0
    for name, number in amount:
        total += number
    return total

if __name__ == "__main__":
    result = orders_sum(orders)

    if result is None:
        print("Lack of data")
    else:
        print("Total sum:", result)

