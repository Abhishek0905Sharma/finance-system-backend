from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date, datetime
from app.models.transaction import TransactionType, TransactionCategory

class TransactionCreate(BaseModel):
    amount: float
    type: TransactionType
    category: TransactionCategory
    description: Optional[str] = None
    date: date

    @field_validator("amount")
    @classmethod
    def amount_positive(cls, v):
        if v <= 0:
            raise ValueError("Amount must be positive")
        return round(v, 2)

    @field_validator("description")
    @classmethod
    def description_length(cls, v):
        if v and len(v) > 300:
            raise ValueError("Description cannot exceed 300 characters")
        return v

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[TransactionType] = None
    category: Optional[TransactionCategory] = None
    description: Optional[str] = None
    date: Optional[date] = None

    @field_validator("amount")
    @classmethod
    def amount_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Amount must be positive")
        return v

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: TransactionType
    category: TransactionCategory
    description: Optional[str]
    date: date
    user_id: int
    created_at: datetime

    model_config = {"from_attributes": True}

class PaginatedTransactions(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[TransactionResponse]
