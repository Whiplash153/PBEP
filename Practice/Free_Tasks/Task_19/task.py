drinks = {
    "cola": {"price": 80, "qty": 10},
    "juice": {"price": 120, "qty": 6},
    "water": {"price": 40, "qty": 25}
}

def get_total_cost(items):
    total = 0
    for item in items.values():
        total += item["price"] * item["qty"]
    return total

def sell(drinks, name, qty):
    if name not in drinks:
        return None

    item = drinks[name]
    if qty > item["qty"]:
        return None

    item["qty"] -= qty
    return item["price"] * qty

if __name__ == "__main__":
    print("Total:", get_total_cost(drinks))
    print("Sell 3 cola:", sell(drinks, "cola", 3))
    print("Sell 20 juice:", sell(drinks, "juice", 20))
    print("Sell water:", sell(drinks, "water", 5))
    print("Updated total:", get_total_cost(drinks))