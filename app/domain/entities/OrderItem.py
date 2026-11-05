from dataclasses import dataclass
from datetime import datetime
@dataclass
class OrderItem:
    _id: str | None = None
    order_id            : int
    product_id          : int
    cantidad            : int    
    created_at          : datetime
    updated_at          : datetime 