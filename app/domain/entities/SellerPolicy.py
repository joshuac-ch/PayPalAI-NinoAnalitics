from dataclasses import dataclass
from datetime import datetime

@dataclass
class SellerPolicy:
    
    offer_max_pct   : int
    umbral_aprobed  : int
    evaluation_days : int
    created_at      : datetime
    updated_at      : datetime
    _id: str | None = None 