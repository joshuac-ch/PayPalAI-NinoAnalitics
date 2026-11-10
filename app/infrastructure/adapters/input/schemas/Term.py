from pydantic import BaseModel
from datetime import datetime

class TermScheme(BaseModel):
    version    : str
    content    : str
    created_at : datetime
    updated_at : datetime 