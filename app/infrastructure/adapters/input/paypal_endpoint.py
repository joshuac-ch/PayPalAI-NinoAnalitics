from fastapi import Depends,APIRouter
from app.infrastructure.adapters.dependencias import adapter_paypal_payment,adapter_paypal_dispute
router=APIRouter()

@router.post("/capture/")
async def get_capture_paypal(order_id:str,adapter_paypal_payment=Depends(adapter_paypal_payment)):
    try:
        return await adapter_paypal_payment.execute(order_id)
    except Exception as e:
        return f"Error en get capture paypal {e}"    

@router.get("/dipute/")
async def get_dispute(paypal_dispute_id:str,adapter_paypal_dispute=Depends(adapter_paypal_dispute)):
    try:
        return await adapter_paypal_dispute.execute(paypal_dispute_id)
    except Exception as e:
        return f"Error get Dispute {e}"        