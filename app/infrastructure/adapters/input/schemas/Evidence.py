from pydantic import BaseModel
from datetime import datetime

class EvidenceScheme(BaseModel):
    
        tipo        :str
        origin      : str
        reference   : str
        analisis    : str
        fecha       : datetime
        created_at  : datetime
        updated_at  : datetime 