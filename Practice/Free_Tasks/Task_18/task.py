class StoreItem:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = int(price)
        self.qty = int(qty)

    def get_total(self):
        return self.price * self.qty

    def add(self, q):
        self.qty += int(q)
        return self.qty

    def remove(self, q):
        q = int(q)
        if q > self.qty:
            raise ValueError("Not enough items")
        self.qty -= q
        return self.qty

def make_list(data):
    result = []
    for name, info in data.items():
        item = StoreItem(name, info["price"], info["qty"])
        result.append(item)
    return result

def calculate_inventory_cost(items):
    total = 0
    for item in items:
        total += item.get_total()
    return total

def sell_item(items, name, qty):
    for item in items:
        if item.name == name:
            try:
                item.remove(qty)
            except ValueError:
                return None
            else:
                return item.price * qty
    return None

if __name__ == "__main__":
    inventory = {
        "apple": {"price": 50, "qty": 120},
        "banana": {"price": 30, "qty": 85},
        "kiwi": {"price": 90, "qty": 40}
    }

    items = make_list(inventory)

    print("Total cost:", calculate_inventory_cost(items))

    print("Sell 5 apples:", sell_item(items, "apple", 5))
    print("Sell 200 bananas:", sell_item(items, "banana", 200))
    print("Sell non-existing item:", sell_item(items, "cola", 1))