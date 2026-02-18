orders = [
    {
        "id": 101,
        "customer": {
            "name": "alice",
            "vip": True
        },
        "payment": {
            "total": 12000,
            "currency": "USD"
        }
    },
    {
        "id": 102,
        "customer": {
            "name": "bob",
            "vip": False
        },
        "payment": {
            "total": 4000,
            "currency": "USD"
        }
    },
    {
        "id": 103,
        "customer": {
            "name": "carol",
            "vip": True
        },
        "payment": {
            "total": 8000,
            "currency": "EUR"
        }
    },
    {
        "id": 104,
        "customer": {
            "name": "dave",
            "vip": True
        },
        "payment": {
            "total": 20000,
            "currency": "USD"
        }
    },
]

filtered = []
for order in orders:

    vip = order["customer"]["vip"]
    currency = order["payment"]["currency"]
    payment = order["payment"]["total"]

    vip_ok = vip
    currency_ok = currency == "USD"
    payment_ok = payment >= 10_000

    if vip_ok and currency_ok and payment_ok:
        filtered.append(order)

result = []
for order in filtered:

    order_id = order["id"]
    order_name = order["customer"]["name"]
    order_total = order["payment"]["total"]

    result.append({
        "order_id": order_id,
        "customer": order_name.upper(),
        "tier": "VIP_PLUS" if order_total >= 15_000 else "VIP",
        "total_k": order_total / 1000
    })

print(result)




































