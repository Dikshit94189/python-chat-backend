# print("user_routes.py loaded")


from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_create import UserCreate
from app.schemas.user_response import UserResponse
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, Form
from app.schemas.user_login import UserLogin
from app.schemas.token import Token
from app.security.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return UserService.register_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post(
    "/login",
    response_model=Token
)
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        return UserService.login_user(
            db,
            username,
            password
        )

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    
@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user