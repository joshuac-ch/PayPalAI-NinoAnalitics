from dataclasses import dataclass
from datetime import datetime

@dataclass
class AuditEvent:
    _id: str | None = None
    order_id    : int
    dispute_id  : int
    actor_type  : str
    accion      : str
    razon       : str
    fecha       : datetime
    created_at  : datetime
    updated_at  : datetime 