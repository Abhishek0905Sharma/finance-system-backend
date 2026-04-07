from pydantic import BaseModel
from typing import Optional

class FinanceSummary(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float
    transaction_count: int

class CategoryBreakdown(BaseModel):
    category: str
    total: float
    count: int
    percentage: float

class MonthlyTotal(BaseModel):
    year: int
    month: int
    income: float
    expense: float
    net: float
