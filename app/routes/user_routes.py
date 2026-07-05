# print("user_routes.py loaded")


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_create import UserCreate
from app.schemas.user_response import UserResponse
from app.services.user_service import UserService

from app.schemas.user_login import UserLogin
from app.schemas.token import Token


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
    user:UserLogin,
    db:Session = Depends(get_db)
):
    
    try:
        
        return UserService.login_user(
            db,
            user.email,
            user.password
        )
    
    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e))