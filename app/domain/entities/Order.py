from dataclasses import dataclass
from datetime import datetime
from app.domain.entities.OrderItem import OrderItem
@dataclass
class Order:
    
    seller_id           : str
    buyer_id            : str
    items               : list[OrderItem]
    monto               : float
    estado              : str
    term_id             : str
    paypal_id           : str
    riesgo              : int
    ubicacion           : str
    terms_accepted_at   : datetime
    created_at          : datetime
    updated_at          : datetime
    _id: str | None = None 