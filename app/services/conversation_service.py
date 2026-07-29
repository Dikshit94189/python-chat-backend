from sqlalchemy.orm import Session

from app.repositories.conversation_repo import ConversationRepository
from fastapi import HTTPException
from sqlalchemy.orm import Session

class ConversationService:

    def __init__(self):
        self.repository  = ConversationRepository()

    def create_conversation(self, db:Session , created_by: int):
        return self.repository.create_conversation(db ,created_by)

     
    # def get_conversation_by_id(self, db: Session, conversation_id: int):
    #     # return self.repository.get_conversation_by_id(id, conversation_id)
    #     return self.repository.get_conversation_by_id(db, conversation_id)

    def get_conversation_by_id(self, db: Session, conversation_id: int):
        conversation = self.repository.get_conversation_by_id(
            db,
            conversation_id
        )

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found"
            )

        return conversation

    def get_all_conversations(self, db:Session):
        return self.repository.get_all_conversations(db)        