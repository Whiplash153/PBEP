users = []

def create_user(name):
    user = {"id": len(users) + 1, "name": name}
    users.append(user)
    return user

def get_users():
    return users

def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"status": "deleted"}