from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, default=0)
    category = Column(String, nullable=False)
    sku = Column(String, unique=True)
    rating = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))