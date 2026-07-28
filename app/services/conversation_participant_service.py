from sqlalchemy.orm import Session

from app.repositories.conversation_participant_repo import (
    ConversationParticipantRepository,
)


class ConversationParticipantService:

    def __init__(self):
        self.repository = ConversationParticipantRepository()

    def create_participant(
        self,
        db: Session,
        conversation_id: int,
        user_id: int
    ):
        return self.repository.create_participant(
            db,
            conversation_id,
            user_id,
        )

    def get_participants_by_conversation(
        self,
        db: Session,
        conversation_id: int,
    ):
        return self.repository.get_participants_by_conversation(
            db,
            conversation_id,
        )