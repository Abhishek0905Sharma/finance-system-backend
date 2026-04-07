from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.analytics import FinanceSummary, CategoryBreakdown, MonthlyTotal
from app.services import analytics_service
from app.middleware.auth import get_current_user, require_role
from app.models.user import User, UserRole

router = APIRouter()

@router.get("/summary", response_model=FinanceSummary)
def summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return analytics_service.get_summary(db, current_user.id)

@router.get("/category-breakdown", response_model=list[CategoryBreakdown])
def category_breakdown(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.analyst, UserRole.admin))
):
    return analytics_service.get_category_breakdown(db, current_user.id)

@router.get("/monthly", response_model=list[MonthlyTotal])
def monthly_totals(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.analyst, UserRole.admin))
):
    return analytics_service.get_monthly_totals(db, current_user.id)
