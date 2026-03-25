from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items")
def get_user_items(user_id: int, limit: int = 10):
    return {
        "user_id": user_id,
        "limit": limit
    }
