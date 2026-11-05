from dataclasses import dataclass
from datetime import datetime
from app.domain.entities.TrackingEvent import TrakingEvent
@dataclass
class Shipment:
    _id: str | None = None
    order_id            : int
    transportista       : str
    numero_seguimiento  : str
    eventos             : list[TrakingEvent]
    firma               : str
    estado              : str
    created_at          : datetime
    updated_at          : datetime 