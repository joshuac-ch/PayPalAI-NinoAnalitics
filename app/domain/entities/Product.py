from dataclasses import dataclass
from datetime import datetime
@dataclass
class Producto:
    _id: str | None = None
    name                : str
    description         : str
    image               : str
    precio              : str
    seller_id           : str
    created_at          : datetime
    updated_at          : datetime 