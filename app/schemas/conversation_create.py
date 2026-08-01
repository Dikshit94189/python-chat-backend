from pydantic import BaseModel

class ConversationCreate(BaseModel):
    receiver_id: int