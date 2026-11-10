from fastapi import APIRouter,Depends
from app.infrastructure.adapters.dependencias import adapter_save_dispute
from app.infrastructure.adapters.input.schemas.Dispute import DisputeScheme
router=APIRouter()

@router.post("/open-dispute/")
async def openDispute(dispute:DisputeScheme,
                      adapter_save_dispute=Depends(adapter_save_dispute)):
    try:
        return await adapter_save_dispute.execute(dispute)        
    except Exception as e:
        return f"Ocurrio un error {e}"    