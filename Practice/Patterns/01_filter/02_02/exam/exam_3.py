transactions = [
    {
        "id": 1,
        "user": {"name": "alice", "verified": True},
        "payment": {"amount": 15000, "status": "success"}
    },
    {
        "id": 2,
        "user": {"name": "bob", "verified": False},
        "payment": {"amount": 20000, "status": "success"}
    },
    {
        "id": 3,
        "user": {"name": "carol", "verified": True},
        "payment": {"amount": 5000, "status": "failed"}
    },
    {
        "id": 4,
        "user": {"name": "dave", "verified": True},
        "payment": {"amount": 30000, "status": "success"}
    },
]

filtered = []
for trans in transactions:

    verified = trans["user"]["verified"]
    amount = trans["payment"]["amount"]
    status = trans["payment"]["status"]

    verify_ok = verified
    amount_ok = amount >= 10_000
    status_ok = status == "success"

    if verify_ok and amount_ok and status_ok:
        filtered.append(trans)

result = []
for trans in filtered:

    trans_id = trans["id"]
    name = trans["user"]["name"]
    amount = trans["payment"]["amount"]

    result.append({
        "tx_id": trans_id,
        "user": name.upper(),
        "size": "BIG" if amount >= 25_000 else "NORMAL",
        "amount_k": amount / 1000
    })

print(result)



