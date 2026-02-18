products = [
    {
        "name": "laptop",
        "pricing": {"price": 120000, "discount": 0.1},
        "stock": {"count": 5}
    },
    {
        "name": "mouse",
        "pricing": {"price": 2000, "discount": 0.0},
        "stock": {"count": 50}
    },
    {
        "name": "monitor",
        "pricing": {"price": 30000, "discount": 0.15},
        "stock": {"count": 12}
    },
]

filtered = []
for product in products:

    price = product["pricing"]["price"]
    count = product["stock"]["count"]

    price_ok = price >= 10_000
    count_ok = count >= 10

    if price_ok and count_ok:
        filtered.append(product)

result = []
for product in filtered:

    name = product["name"]
    price = product["pricing"]["price"]
    discount = product["pricing"]["discount"]
    count = product["stock"]["count"]

    result.append({
        "product": name.upper(),
        "final_price": price * (1 - discount),
        "stock_level": "LOW" if count < 20 else "OK"
    })

print(result)