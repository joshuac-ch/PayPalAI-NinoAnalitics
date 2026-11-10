from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserModel(BaseModel):
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