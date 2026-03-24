from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def get_product_id(product_id: int):
    return {"product_id": product_id}

@app.get("/products/{product_id}/reviews")
def product_reviews(product_id: int, limit: int = 5):
    return {
        "product_id": product_id,
        "limit": limit
    }