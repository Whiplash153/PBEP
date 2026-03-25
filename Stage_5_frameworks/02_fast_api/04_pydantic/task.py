from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int | None = Field(default=None, ge=0)

@app.post("/users")
def add_user(user: User):
    return {
        "message": "user_created",
        "data": user
    }

@app.get("/users")
def get_users():
    return {"users": []}