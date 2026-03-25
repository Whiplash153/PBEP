from sqlalchemy.orm import Session
from models import User, Order

# CREATE

def create_user(session: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    session.add(user)
    return user

def create_order(session: Session, user_id: int, status: str, total: int) -> Order:
    order = Order(user_id=user_id, status=status, total=total)
    session.add(order)
    return order

# READ

def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def get_orders_by_user(session: Session, user_id: int) -> list[Order]:
    return session.query(Order).filter(Order.user_id == user_id).all()

# UPDATE

def update_user_email(session: Session, user_id: int, new_email: str) -> None:
    user = session.get(User, user_id)
    if user:
        user.email = new_email

# DELETE

def delete_user(session: Session, user_id: int) -> None:
    user = session.get(User, user_id)
    if user:
        session.delete(user)