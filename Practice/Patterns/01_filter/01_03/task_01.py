products = [
    {"name": "laptop",      "price": 1200, "discount": 10, "category": "tech"},
    {"name": "sofa",        "price": 800,  "discount": 0,  "category": "furniture"},
    {"name": "smartphone",  "price": 900,  "discount": 5,  "category": "tech"},
    {"name": "chair",       "price": 200,  "discount": 0,  "category": "furniture"},
    {"name": "tablet",      "price": 400,  "discount": 15, "category": "tech"},
]

filtered = []
for product in products:
    if product["category"] == "tech" and product["discount"] < 15 and product["price"] >= 500:
        filtered.append(product)

result = []
for product in filtered:
    final_price = product["price"] - product["price"] * product["discount"] / 100

    result.append({
        "product": product["name"].upper(),
        "final_price": final_price,
        "tag": "PREMIUM" if final_price > 1000 else "STANDARD"
    })

print("Result:", result)
