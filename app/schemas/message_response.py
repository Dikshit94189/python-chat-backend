from datetime import datetime
from pydantic import BaseModel

class MessageResponse(BaseModel):
    id:int
    conversation_id:int
    sender_id:int
    message:str
    created_at:datetime
    
    class config:
        from_attributes = True