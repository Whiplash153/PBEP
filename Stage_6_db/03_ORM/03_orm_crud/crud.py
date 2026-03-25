from sqlalchemy.orm import Session
from engine1 import engine
from model1 import User

# CREATE
def create_user(name: str, email: str):
    with Session(engine) as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        return user

#READ
def get_all_users():
    with Session(engine) as session:
        users = session.query(User).all()
        return users

#READ
def get_user_by_id(user_id: int):
    with Session(engine) as session:
        user = session.query(User).filter(User.id == user_id).first()
        return user

#UPDATE
def update_user_email(user_id: int, new_email: str):
    with Session(engine) as session:
        user = session.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        user.email = new_email
        session.commit()
        return user

#DELETE
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.query(User).filter(User.id == user_id).first()

        if not user:
            return False

        session.delete(user)
        session.commit()
        return True

