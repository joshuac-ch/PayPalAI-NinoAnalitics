from dataclasses import dataclass
from datetime import datetime

@dataclass
class Term:
   
    version    : str
    content    : str
    created_at : datetime
    updated_at : datetime 
    _id: str | None = None