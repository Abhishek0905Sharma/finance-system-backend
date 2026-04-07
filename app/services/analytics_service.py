from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction, TransactionType

def get_summary(db: Session, user_id: int) -> dict:
    rows = db.query(Transaction.type, func.sum(Transaction.amount), func.count(Transaction.id))\
             .filter(Transaction.user_id == user_id)\
             .group_by(Transaction.type).all()
    income = expense = count = 0
    for t, total, c in rows:
        if t == TransactionType.income:
            income = round(total, 2)
        else:
            expense = round(total, 2)
        count += c
    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": round(income - expense, 2),
        "transaction_count": count
    }

def get_category_breakdown(db: Session, user_id: int) -> list:
    rows = db.query(Transaction.category, func.sum(Transaction.amount), func.count(Transaction.id))\
             .filter(Transaction.user_id == user_id)\
             .group_by(Transaction.category).all()
    total_all = sum(r[1] for r in rows) or 1
    return [
        {
            "category": r[0].value,
            "total": round(r[1], 2),
            "count": r[2],
            "percentage": round((r[1] / total_all) * 100, 2)
        }
        for r in rows
    ]

def get_monthly_totals(db: Session, user_id: int) -> list:
    rows = db.query(
        extract("year", Transaction.date).label("year"),
        extract("month", Transaction.date).label("month"),
        Transaction.type,
        func.sum(Transaction.amount)
    ).filter(Transaction.user_id == user_id)\
     .group_by("year", "month", Transaction.type)\
     .order_by("year", "month").all()

    months = {}
    for year, month, t, total in rows:
        key = (int(year), int(month))
        if key not in months:
            months[key] = {"year": key[0], "month": key[1], "income": 0.0, "expense": 0.0}
        if t == TransactionType.income:
            months[key]["income"] = round(total, 2)
        else:
            months[key]["expense"] = round(total, 2)

    result = []
    for v in months.values():
        v["net"] = round(v["income"] - v["expense"], 2)
        result.append(v)
    return result
