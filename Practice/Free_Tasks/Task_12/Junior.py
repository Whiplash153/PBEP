orders = [
    ("croissant", 120),
    ("baguette", 80),
    ("eclair", 150),
]

def orders_sum(orders_list):
    if not orders_list:
        return None

    total = 0
    for order in orders_list:
        name = order[0]
        price = order[1]
        total += price

    return total


if __name__ == "__main__":
    result = orders_sum(orders)

    if result is None:
        print("No orders today.")
    else:
        print(f"Total sum: {result}")