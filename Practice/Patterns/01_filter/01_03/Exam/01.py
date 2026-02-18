orders = [
    {"id": 1, "customer": {"name": "bob", "vip": False}, "items": 3, "total": 120},
    {"id": 2, "customer": {"name": "alice", "vip": True},  "items": 1, "total": 200},
    {"id": 3, "customer": {"name": "mike", "vip": False}, "items": 5, "total": 80},
    {"id": 4, "customer": {"name": "kate", "vip": True},  "items": 2, "total": 150},
]

filtered = []
for order in orders:

    items_ok = order["items"] >= 2
    total_ok = order["total"] >= 100
    client_ok = order["customer"]["vip"] or order["total"] >= 150

    if items_ok and total_ok and client_ok:
        filtered.append(order)

result = []
for order in filtered:

    if order["customer"]["vip"]:
        bonus = 20
    else:
        bonus = 0

    final_total = order["total"] + bonus
    vip = order["customer"]["vip"]

    result.append({
        "order_id": order["id"],
        "customer": order["customer"]["name"].upper(),
        "final_total": final_total,
        "tag": "VIP" if vip else "REGULAR"
    })

print(result)