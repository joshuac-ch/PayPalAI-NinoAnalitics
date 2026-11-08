from dataclasses import dataclass
from datetime import datetime
@dataclass
class OrderItem:
   
    order_id            : str
    product_id          : str
    cantidad            : int    
    created_at          : datetime
    updated_at          : datetime 
    _id: str | None = None