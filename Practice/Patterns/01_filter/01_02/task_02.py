products = [
    {"name": "milk",  "price": 120, "category": "food"},
    {"name": "tv",    "price": 55000, "category": "electronics"},
    {"name": "bread", "price": 40, "category": "food"},
    {"name": "phone", "price": 30000, "category": "electronics"},
    {"name": "water", "price": 25, "category": "food"},
]


filtered = []
for p in products:
    if p["category"] == "food" and p["price"] > 50:
        filtered.append(p)

result = []
for item in filtered:
    result.append({
        "Title": item["name"],
        "Cost": item["price"] * 0.9
    })

print(result)