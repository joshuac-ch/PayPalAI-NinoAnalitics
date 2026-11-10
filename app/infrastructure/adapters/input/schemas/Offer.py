from pydantic import BaseModel
from datetime import datetime

class OfferScheme(BaseModel):
        monto           : float
        tipo            : str
        propuesta_por   : str
        razon           : str
        estado          : str
        created_at      : datetime
        updated_at      : datetime