from sqlalchemy.orm import Session

from app.models.message import Message
from app.repositories.message_repo import MessageRepository
from app.schemas.message_create import MessageCreate


class MessageService:

    @staticmethod
    def send_message(
        db: Session,
        sender_id: int,
        message_data: MessageCreate
    ):

        message = Message(
            conversation_id=message_data.conversation_id,
            sender_id=sender_id,
            message=message_data.message
        )

        return MessageRepository.create_message(
            db,
            message
        )

    @staticmethod
    def get_messages(
        db: Session,
        conversation_id: int
    ):
        return MessageRepository.get_messages_by_conversation(
            db,
            conversation_id
        )