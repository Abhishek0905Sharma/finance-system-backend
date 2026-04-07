from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse, UserLogin, TokenResponse
from app.services import user_service
from app.middleware.auth import get_current_user, require_role
from app.models.user import UserRole

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)

@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    return user_service.login_user(db, data.username, data.password)

@router.get("/me", response_model=UserResponse)
def me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), _=Depends(require_role(UserRole.admin))):
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), _=Depends(require_role(UserRole.admin))):
    return user_service.get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db), _=Depends(require_role(UserRole.admin))):
    return user_service.update_user(db, user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), _=Depends(require_role(UserRole.admin))):
    return user_service.delete_user(db, user_id)
