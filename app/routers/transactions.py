from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
from app.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse, PaginatedTransactions
from app.services import transaction_service
from app.middleware.auth import get_current_user, require_role
from app.models.user import User, UserRole
from app.models.transaction import TransactionType, TransactionCategory

router = APIRouter()

@router.post("/", response_model=TransactionResponse, status_code=201)
def create(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.analyst, UserRole.admin))
):
    return transaction_service.create_transaction(db, data, current_user.id)

@router.get("/", response_model=PaginatedTransactions)
def list_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    type: Optional[TransactionType] = None,
    category: Optional[TransactionCategory] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return transaction_service.get_transactions(
        db, current_user.id, page, page_size,
        type, category, start_date, end_date, min_amount, max_amount
    )

@router.get("/{tx_id}", response_model=TransactionResponse)
def get_transaction(tx_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return transaction_service.get_transaction_by_id(db, tx_id, current_user.id)

@router.put("/{tx_id}", response_model=TransactionResponse)
def update_transaction(
    tx_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.analyst, UserRole.admin))
):
    return transaction_service.update_transaction(db, tx_id, current_user.id, data)

@router.delete("/{tx_id}")
def delete_transaction(
    tx_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.admin))
):
    return transaction_service.delete_transaction(db, tx_id, current_user.id)
