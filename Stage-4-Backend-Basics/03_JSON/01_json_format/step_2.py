product_dict = {
    "id": 1,
    "name": "Notebook",
    "price": 999.99,
    "in_stock": True,
    "tags": ["electronics", "office"],
    "description": None
}

product_json = """
{
    "id": 1,
    "name": "Notebook",
    "price": 999.99,
    "in_stock": true,
    "tags": ["electronics", "office"],
    "description": null
}
"""

print("Type of product_dict:")
print(type(product_dict))

print("\nType of product_json:")
print(type(product_json))