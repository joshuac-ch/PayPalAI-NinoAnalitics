from dataclasses import dataclass
from datetime import datetime

@dataclass
class Term:
    _id: str | None = None
    version    : str
    content    : str
    created_at : datetime
    updated_at : datetime 