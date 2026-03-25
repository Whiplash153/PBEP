from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: int = Field(gt=0)
    age: int | None = Field(default=None, ge=0)

@app.post("/products")
def create_product(product:Product):
    return {
        "message": "product created",
        "data": product
    }