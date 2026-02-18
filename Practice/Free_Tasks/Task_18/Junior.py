inventory = {
    "apple": {"price": 50, "qty": 120},
    "banana": {"price": 30, "qty": 85},
    "kiwi": {"price": 90, "qty": 40}
}

class StoreItem:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty

    def remove(self, q):
        if q > self.qty:
            print("Not enough in stock")
        else:
            self.qty -= q


def make_list(data):
    items = []
    for name, info in data.items():
        item = StoreItem(name, info["price"], info["qty"])
        items.append(item)
    return items


def total_cost(items):
    total = 0
    for i in items:
        total += i.total()
    return total


def sell(items, name, q):
    for item in items:
        if item.name == name:
            if q > item.qty:
                print("Not enough in stock")
                return None
            item.qty -= q
            return item.price * q

    print("Item not found")
    return None


# запуск программы
items = make_list(inventory)

print("Total:", total_cost(items))
print("Sell apple:", sell(items, "apple", 5))
print("Sell cola:", sell(items, "cola", 1))
print("Sell banana:", sell(items, "banana", 200))