from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Base, User, Post

engine = create_engine(
    "postgresql+psycopg2://msh:123@localhost/orm_bd",
    echo=True
)

Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="Anna")

    post1 = Post(title="First post")
    post2 = Post(title="Second post")

    user.posts.append(post1)
    user.posts.append(post2)

    session.add(user)
    session.commit()

    print("User ID:", user.id)
    print("Post1 user_id", post1.user_id)
    print("Post 2 user_id:", post2.user_id)