from dataclasses import dataclass
from datetime import datetime

@dataclass
class Evidence:
    
    tipo        :str
    origin      : str
    reference   : str
    analisis    : str
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime 
    _id: str | None = None