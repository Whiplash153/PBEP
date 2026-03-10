from sqlalchemy import create_engine
from  sqlalchemy.orm import Session
from model import Base, User, Post

engine = create_engine (
    "postgresql+psycopg2://msh:123@localhost/orm_bd",
    echo=True
)

Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="TaskUser")

    post1 = Post(title="Task Post 1")
    post2 = Post(title="Task Post 2")
    post3 = Post(title="Task Post 3")

    user.posts.append(post1)
    user.posts.append(post2)
    user.posts.append(post3)

    session.add(user)
    session.commit()

    print("User ID:", user.id)
    print("User posts:", user.posts)
    print("User name:", user.name)

with Session(engine) as session:
    db_user = session.query(User).first()
    print("User:", db_user.name)

    for post in db_user.posts:
        print("—", post.title)

    db_post = session.query(Post).first()
    print("Post author:", db_post.user.name)

