from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.conversation_response import ConversationResponse
from app.services.conversation_service import ConversationService
from app.security.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)

conversation_service = ConversationService()


@router.post("/", response_model=ConversationResponse)
def create_conversation(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return conversation_service.create_conversation(
        db,
        created_by=current_user.id
    )


@router.get("/", response_model=list[ConversationResponse])
def get_all_conversations(db: Session = Depends(get_db)):
    return conversation_service.get_all_conversations(db)


@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    return conversation_service.get_conversation_by_id(
        db,
        conversation_id
    )