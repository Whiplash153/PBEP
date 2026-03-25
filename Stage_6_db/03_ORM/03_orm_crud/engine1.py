from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://msh:123@localhost:5432/orm_bd"

engine = create_engine (
    DATABASE_URL,
    echo=True
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result)

print(engine)
