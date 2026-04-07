import enum
from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"

class TransactionCategory(str, enum.Enum):
    salary = "salary"
    food = "food"
    transport = "transport"
    entertainment = "entertainment"
    utilities = "utilities"
    healthcare = "healthcare"
    education = "education"
    shopping = "shopping"
    investment = "investment"
    other = "other"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    category = Column(Enum(TransactionCategory), nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="transactions")
