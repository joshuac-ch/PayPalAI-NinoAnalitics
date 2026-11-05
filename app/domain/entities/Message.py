from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    _id: str | None = None
    author      : str
    content     : str 
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime 