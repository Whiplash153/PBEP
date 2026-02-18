orders = [
    {"id": 1, "user": "alice", "amount": 1200, "status": "paid"},
    {"id": 2, "user": "bob",   "amount": 300,  "status": "pending"},
    {"id": 3, "user": "mike",  "amount": 1500, "status": "paid"},
    {"id": 4, "user": "kate",  "amount": 200,  "status": "canceled"},
    {"id": 5, "user": "john",  "amount": 2500, "status": "paid"},
]

filtered = []
for order in orders:
    if order["status"] == "paid" and order["amount"] > 1000:
        filtered.append(order)

result = []
for order in filtered:
    result.append({
        "order_id": order["id"],
        "customer": order["user"].upper(),
        "total": order["amount"] * 1.2
    })

print(result)