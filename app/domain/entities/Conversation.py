from dataclasses import dataclass
from datetime import datetime
from app.domain.entities.Message import Message

@dataclass
class Conversation:
    _id: str | None = None
    messages    : list[Message]
    dispute_id  : int
    created_at  : datetime
    updated_at  : datetime 