from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_create import UserCreate
from app.repositories.user_repo import UserRepository

class UserService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):

        # Check if email already exists
        existing_user = UserRepository.get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            # raise HTTPException(status_code=400,detail="Email already exists")
            raise Exception("Email already exists")
            

        user = User(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password
        )

        return UserRepository.create_user(db, user)