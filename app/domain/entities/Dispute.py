from dataclasses import dataclass
from datetime import datetime

from app.domain.entities.Evidence import Evidence
from app.domain.entities.Offer import Offer
@dataclass
class Dispute:
    _id: str | None = None
    order_id        : int
    seller_id       : int
    buyer_id        : int
    paypal_id       : int
    motivo          : str
    estado          : str
    monto           : float 
    fecha_limite    : datetime
    offers          : list[Offer]
    evidences       : list[Evidence]
    clasification   : str
    line_time       : list[str]
    resultado       : str
    created_at      : datetime
    updated_at      : datetime  
