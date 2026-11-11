from app.domain.ports.dispute_port import DisputePort
from app.domain.ports.order_port import OrderPort
class SaveDisputeUseCase:

    def __init__(self,dispute_port:DisputePort,order_port:OrderPort):
        self.dispute_port=dispute_port
        self.order_port=order_port

    async def create_dispute(self,dispute):
        try:
            return await self.dispute_port.save(dispute)
        except Exception as e:
            return f"Ocurrio un error en create_dispute {e}"

    async def execute(self,dispute):
        try:
            valid_order=await self.order_port.get(dispute.order_id)
            if not valid_order:
                raise ValueError("No existe una order para abrir esta disputa")
            
            print("Creando Dispute")
            await self.create_dispute(dispute)
            print("Dispute creada exitosamente")
            
            return {
                "status":"success"
            }
        except Exception as e:
             return f"Error en create_dispute {e}"