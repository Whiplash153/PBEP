from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int | None = None

@app.post("/users", status_code=201)
def add_user(user: User):
    if user.age is not None and user.age < 0:
        raise HTTPException(status_code=400, detail="Age cannot be negative")

    return {
        "message": "user_created",
        "data": user
    }

@app.get("/users")
def get_users():
    return {"users": []}