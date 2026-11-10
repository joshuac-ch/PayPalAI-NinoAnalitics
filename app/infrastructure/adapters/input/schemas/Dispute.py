from pydantic import BaseModel
from datetime import datetime
from app.infrastructure.adapters.input.schemas.Evidence import EvidenceScheme
from app.infrastructure.adapters.input.schemas.Offer import OfferScheme

class DisputeScheme(BaseModel):
    order_id        : str
    seller_id       : str
    buyer_id        : str
    paypal_id       : str
    motivo          : str
    estado          : str
    monto           : float 
    fecha_limite    : datetime
    offers          : list[OfferScheme]
    evidences       : list[EvidenceScheme]
    clasification   : str
    line_time       : list[str]
    resultado       : str
    created_at      : datetime
    updated_at      : datetime  
