from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_create import UserCreate
from app.repositories.user_repo import UserRepository
from app.security.auth import hash_password

from app.security.auth import create_access_token
from app.security.auth import verify_password

class UserService:

    @staticmethod
    def register_user(db: Session, user_data: UserCreate):

        existing_user = UserRepository.get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise Exception("Email already exists")

#  MAIN CODE FOR THE PASSWORD ENCRYPT
        # user = User(
        #     name=user_data.name,
        #     email=user_data.email,
        #     password=hash_password(user_data.password)   # <-- IMPORTANT
        # )

        #  CODE FOR THE TEMPORARLY FOR THE PASSWORD ENCRYPT OR DECRYPT

        hashed = hash_password(user_data.password)

        print("=" * 40)
        print("Original :", user_data.password)
        print("Hashed   :", hashed)
        print("=" * 40)

        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hashed
        )
        return UserRepository.create_user(db, user)
    

    @staticmethod
    def login_user(db: Session, email: str, password: str):

        user = UserRepository.get_user_by_email(
            db,
            email
            )

        if not user:
            raise Exception("Invalid email or password")

        if not verify_password(
            password,
            user.password
            ):
            raise Exception("Invalid email or password")

        token = create_access_token(
            {
                "user_id": user.id,
                "email": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }