from engine import engine
from models import Base
from sqlalchemy.orm import Session
from crud import (
create_user,
create_order,
get_user_by_id,
get_orders_by_user,
update_user_email,
delete_user
)


def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        # CREATE
        user = create_user(session, "Anna", "anna1@test.com")
        session.flush()

        create_order(session, user.id, "created", 500)
        create_order(session, user.id, "paid", 1200)
        session.commit()

        # READ
        db_user = get_user_by_id(session, user.id)
        print("User:", db_user.name)

        orders = get_orders_by_user(session, user.id)
        print("\nOrders count:", len(orders))

        # UPDATE
        update_user_email(session, user.id, "new_anna@test.com")
        session.commit()

        updated_user = get_user_by_id(session, user.id)
        print("\nUpdated email:", updated_user.email)

        # DELETE
        delete_user(session, user.id)
        session.commit()

        print("User deleted.")

if __name__ == "__main__":
    main()