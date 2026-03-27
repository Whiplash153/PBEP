from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

users = []
next_id = 1

class User(BaseModel):
    id: int | None = None
    name: str = Field(min_length=2, max_length=50)
    age: int | None = Field(default=None, ge=0)

@app.post("/users", status_code=201)
def add_user(user: User):
    global next_id

    user.id = next_id
    next_id += 1

    users.append(user)

    return {
        "message": "user_created",
        "data": user
    }

@app.get("/users")
def get_all_users():
    return {"users": users}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="No user with such id")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "user_deleted"}

    raise HTTPException(status_code=404, detail="No user with such id")