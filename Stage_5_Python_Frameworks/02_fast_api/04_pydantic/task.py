from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def add_user(user: User):
    return {
        "message": "user_created",
        "data": user
    }

@app.get("/users")
def get_users():
    return {"users": []}