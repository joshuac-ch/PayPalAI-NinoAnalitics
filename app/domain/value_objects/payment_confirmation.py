from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

@dataclass
class PaymentConfirmation:
    capture_id:str
    status:str
    amount:Decimal
    currency:str
    created_at:datetime | None = None