import json

product = {
    "id": 1,
    "name": "Notebook",
    "price": 999.99,
    "in_stock": True,
    "tags": ["electronics", "office"],
    "description": None
}

json_text = json.dumps(product)

print(json_text)