from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderItem(BaseModel):
    order_id            : str
    product_id          : str
    cantidad            : int    
    created_at          : datetime
    updated_at          : datetime 