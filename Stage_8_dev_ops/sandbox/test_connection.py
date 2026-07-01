from sqlalchemy import text
from session import SessionLocal

session = SessionLocal()

result = session.execute(text("SELECT 1"))

print(result.scalar())

session.close()