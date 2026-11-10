from pydantic import BaseModel
from datetime import datetime

class ProductoSchema(BaseModel):
    name                : str
    description         : str
    image               : str
    precio              : str
    seller_id           : str
    created_at          : datetime
    updated_at          : datetime 