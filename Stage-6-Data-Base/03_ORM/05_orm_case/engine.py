from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://msh:123@localhost:5432/case_orm"

engine = create_engine(
    DATABASE_URL,
    echo=True
)