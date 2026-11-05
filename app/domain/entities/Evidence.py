from dataclasses import dataclass
from datetime import datetime

@dataclass
class Evidence:
    _id: str | None = None
    tipo        :str
    origin      : str
    reference   : str
    analisis    : str
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime 
    