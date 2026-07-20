from sqlalchemy.orm import Session

from app.models.conversation import Conversation


class ConversationRepository:

    def create_conversation(self, db: Session):
        conversation = Conversation()

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def get_conversation_by_id(self, db: Session, conversation_id: int):
        return (
            db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

    def get_all_conversations(self, db: Session):
        return db.query(Conversation).all()