from dataclasses import dataclass
from datetime import datetime
@dataclass
class Producto:
    id                  : int
    name                : str
    description         : str
    image               : str
    precio              : str
    seller_id           : str
    created_at          : datetime
    updated_at          : datetime 