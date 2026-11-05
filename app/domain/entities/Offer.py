from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass
class Offer:
    _id: str | None = None
    monto           : float
    tipo            : str
    propuesta_por   : Enum["cliente","vendedor"]
    razon           : str
    estado          : str
    created_at      : datetime
    updated_at      : datetime
    
