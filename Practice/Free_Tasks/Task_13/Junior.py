purchases = {
    "Ivan": [1200, 800, 350],
    "Anna": [200, 450],
    "Oleg": []
}

def get_top_customers(data):
    if not data:
        return None

    top_name = ""
    top_sum = 0

    for name in data:
        summary = data[name]          # достаём список по ключу
        customer_sum = sum(summary)   # считаем сумму покупок

        if customer_sum > top_sum:    # сравниваем с текущим максимумом
            top_sum = customer_sum
            top_name = name

    if top_sum == 0:
        return None

    return top_name


if __name__ == "__main__":
    result = get_top_customers(purchases)
    if result is None:
        print("Нет данных о покупках.")
    else:
        print(f"Топовый клиент: {result}")