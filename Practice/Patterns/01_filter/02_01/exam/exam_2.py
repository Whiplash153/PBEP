orders = [
    {"id": 1, "amount": 1200, "status": "completed"},
    {"id": 2, "amount": 300,  "status": "cancelled"},
    {"id": 3, "amount": 700,  "status": "completed"},
    {"id": 4, "amount": 1500, "status": "completed"},
    {"id": 5, "amount": 400,  "status": "pending"},
]

filtered = []
for order in orders:

    status = order["status"]
    amount = order["amount"]

    status_ok = status == "completed"
    amount_ok = amount >= 500

    if status_ok and amount_ok:
        filtered.append(order)

result = []
for order in filtered:

    amount = order["amount"]
    id = order["id"]

    result.append({
        "order_id": id,
        "amount": amount,
        "level": "HIGH" if amount >= 1000 else "NORMAL"
    })

print(result)