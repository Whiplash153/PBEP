import json

json_text = """
{
    "id": 1,
    "name": "Notebook",
    "price": 999.99,
    "in_stock": true,
    "tags": ["electronics", "office"],
    "description": null
}
"""

product = json.loads(json_text)

print(product)
