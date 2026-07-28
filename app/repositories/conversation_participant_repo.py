from sqlalchemy.orm import Session

from app.models.conversation_participant import ConversationParticipant


class ConversationParticipantRepository:

    def create_participant(
        self,
        db: Session,
        conversation_id: int,
        user_id: int
    ):
        participant = ConversationParticipant(
            conversation_id=conversation_id,
            user_id=user_id
        )

        db.add(participant)
        db.commit()
        db.refresh(participant)

        return participant

    def get_participants_by_conversation(
        self,
        db: Session,
        conversation_id: int
    ):
        return (
            db.query(ConversationParticipant)
            .filter(
                ConversationParticipant.conversation_id == conversation_id
            )
            .all()
        )