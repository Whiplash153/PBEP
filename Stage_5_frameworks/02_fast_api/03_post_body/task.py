from fastapi import FastAPI

app = FastAPI()

@app.post("/products")
def create_product(product: dict):
    name = product["name"]
    price = product["price"]

    return {
        "message": "product created",
        "name": name,
        "price": price,
        "data": product
    }

@app.get("/products")
def get_products():
    return {"products": []}
