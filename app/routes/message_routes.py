from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.message_create import MessageCreate
from app.schemas.message_response import MessageResponse
from app.security.auth import get_current_user
from app.services.message_service import MessageService

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/", response_model=MessageResponse)
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MessageService.send_message(
        db=db,
        sender_id=current_user.id,
        message_data=message
    )


@router.get("/{conversation_id}", response_model=list[MessageResponse])
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    return MessageService.get_messages(
        db,
        conversation_id
    )