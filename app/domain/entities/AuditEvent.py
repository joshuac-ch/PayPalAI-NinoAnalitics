from dataclasses import dataclass
from datetime import datetime

@dataclass
class AuditEvent:
    
    order_id    : str
    dispute_id  : str
    actor_type  : str
    accion      : str
    razon       : str
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime
    _id: str | None = None 