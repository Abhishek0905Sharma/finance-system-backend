from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException
from datetime import date
from typing import Optional
from app.models.transaction import Transaction, TransactionType, TransactionCategory
from app.schemas.transaction import TransactionCreate, TransactionUpdate

def create_transaction(db: Session, data: TransactionCreate, user_id: int) -> Transaction:
    tx = Transaction(**data.model_dump(), user_id=user_id)
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transactions(
    db: Session,
    user_id: int,
    page: int = 1,
    page_size: int = 20,
    type: Optional[TransactionType] = None,
    category: Optional[TransactionCategory] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    if type:
        query = query.filter(Transaction.type == type)
    if category:
        query = query.filter(Transaction.category == category)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    if min_amount is not None:
        query = query.filter(Transaction.amount >= min_amount)
    if max_amount is not None:
        query = query.filter(Transaction.amount <= max_amount)

    total = query.count()
    items = query.order_by(Transaction.date.desc()).offset((page - 1) * page_size).limit(page_size).all()
    return {"total": total, "page": page, "page_size": page_size, "items": items}

def get_transaction_by_id(db: Session, tx_id: int, user_id: int) -> Transaction:
    tx = db.query(Transaction).filter(Transaction.id == tx_id, Transaction.user_id == user_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

def update_transaction(db: Session, tx_id: int, user_id: int, data: TransactionUpdate) -> Transaction:
    tx = get_transaction_by_id(db, tx_id, user_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(tx, field, value)
    db.commit()
    db.refresh(tx)
    return tx

def delete_transaction(db: Session, tx_id: int, user_id: int):
    tx = get_transaction_by_id(db, tx_id, user_id)
    db.delete(tx)
    db.commit()
    return {"message": f"Transaction {tx_id} deleted"}
