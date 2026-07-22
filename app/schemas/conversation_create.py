from pydantic import BaseModel

class ConservationCreate(BaseModel):
    receiver_id: int