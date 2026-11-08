from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    
    author      : str
    content     : str 
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime 
    _id: str | None = None 