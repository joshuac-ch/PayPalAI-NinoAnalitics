from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrakingEvent:
    id                  : int
    estado              : str
    lugar               : str
    fecha               : datetime
    ubicacion_entrega   : str
    created_at          : datetime
    updated_at          : datetime