from dataclasses import dataclass
from datetime import datetime
from app.domain.entities.OrderItem import OrderItem
@dataclass
class Order:
    _id: str | None = None
    seller_id           : int
    buyer_id            : int
    items               : list[OrderItem]
    monto               : float
    estado              : str
    term_id             : int
    paypal_id           : int
    riesgo              : int
    terms_accepted_at   : datetime
    created_at          : datetime
    updated_at          : datetime 