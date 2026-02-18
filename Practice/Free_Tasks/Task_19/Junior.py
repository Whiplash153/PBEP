drinks = {
    "cola": {"price": 80, "qty": 10},
    "juice": {"price": 120, "qty": 6},
    "water": {"price": 40, "qty": 25}
}

def get_total_cost(items):
    total = 0
    for name in items:
        price = items[name]["price"]
        qty = items[name]["qty"]
        total += price * qty
    print("Total cost is:", total)   # джун печатает вместо return
    return total


def sell(drinks, name, qty):
    if name not in drinks:
        print("No such drink")       # джун пишет сообщения прямо здесь
        return None

    item = drinks[name]
    if qty > item["qty"]:
        print("Not enough in stock") # опять print
        return None

    item["qty"] -= qty
    total_price = item["price"] * qty
    print("Sold for:", total_price)  # джун печатает результат
    return total_price


# запуск программы
get_total_cost(drinks)                # джун не пишет main-блок
sell(drinks, "cola", 3)
sell(drinks, "juice", 20)
sell(drinks, "water", 5)
get_total_cost(drinks)