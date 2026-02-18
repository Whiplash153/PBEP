products = {
    "apple": 100,
    "banana": 60,
    "cherry": 200,
    "milk": 120,
    "bread": 80
}

cart = ["apple", "milk", "cherry", "coffee"]

available = set(products) & set(cart)
missing = set(cart) - set(products)

total = sum(products[item] for item in available)
print("Total:", total)
print("Missing:", missing)

