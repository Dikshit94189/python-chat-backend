from sqlalchemy import Column, Integer, DateTime , ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id= Column(Integer, primary_key=True, index=True)

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )