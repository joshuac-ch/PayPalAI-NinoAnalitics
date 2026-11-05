from dataclasses import dataclass
from datetime import datetime
@dataclass
class User:    
    name        :       str
    last        :       str
    tel         :       int
    email       :       str
    profile     :       str
    username    :       str
    password    :       str
    tipo        :       str
    created_at  :       datetime
    updated_at  :       datetime
    _id         : str | None = None