from app.infrastructure.adapters.dependencias import adapter_get_user
from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter()

@router.get("/g/id/")
async def find_users_id(id:int):
    try:
        return await adapter_get_user.find_user_id(id)        
    except Exception as e:
        ValueError(f"Ocurrio un error en find_users_id {e}") 