from dataclasses import dataclass
from datetime import datetime
from app.domain.entities.Message import Message

@dataclass
class Conversation:
   
    messages    : list[Message]
    dispute_id  : str
    created_at  : datetime
    updated_at  : datetime 
    _id: str | None = None