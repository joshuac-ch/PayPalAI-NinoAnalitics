from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.infrastructure.adapters.input.schemas.OrderItem import OrderItem

class OrderScheme(BaseModel):
    seller_id           : str
    buyer_id            : str
    items               : list[OrderItem]
    monto               : float=1.0
    estado              : str
    term_id             : str
    
    paypal_order_id: str | None
    paypal_capture_id: str | None
    
    payment_status: str="PENDING"
    currency: str="USD"
    
    riesgo              : int
    ubicacion           : str
    terms_accepted_at   : datetime
    created_at          : datetime
    updated_at          : datetime
    _id: str | None = None 