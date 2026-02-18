products = [
    {"name": "laptop",      "price": 120000, "sold": 120, "rating": 4.3, "category": "electronics"},
    {"name": "headphones",  "price": 8000,   "sold": 500, "rating": 4.7, "category": "electronics"},
    {"name": "coffee",      "price": 300,    "sold": 1500, "rating": 4.1, "category": "grocery"},
    {"name": "monitor",     "price": 30000,  "sold": 200, "rating": 4.8, "category": "electronics"},
    {"name": "sneakers",    "price": 9000,   "sold": 350, "rating": 4.6, "category": "fashion"},
]

filtered = []
for product in products:

    category = product["category"]
    price = product["price"]
    sold = product["sold"]
    rating = product["rating"]

    category_ok = category == "electronics"
    price_ok = price >= 10000
    sold_ok = sold >= 150
    rating_ok = rating >= 4.5

    if category_ok and price_ok and sold_ok and rating_ok:
        filtered.append(product)

result = []
for product in filtered:

    category = product["category"]
    price = product["price"]
    sold = product["sold"]
    rating = product["rating"]

    if sold >= 300:
        popularity = "TOP"
    elif sold >= 150:
        popularity = "MID"
    else:
        popularity = "LOW"

    result.append({
        "product": product["name"].upper(),
        "revenue": price * sold,
        "popularity": popularity
    })

print(result)
