from app.domain.ports.order_port import OrderPort
from app.domain.ports.term_port import TermPort
from app.domain.ports.product_port import ProductPort
from app.domain.ports.shipment_port import ShipmentPort
from app.domain.ports.paypal_payment_gateway_port import PaypalPaymentGatewayPort

import uuid
from datetime import datetime,timezone,date
from decimal import Decimal
class SaveOrderUseCase:

    def __init__(self,order_port:OrderPort,shipment_port:ShipmentPort,paypal_payments_port:PaypalPaymentGatewayPort):
        self.order_port=order_port
        self.shipment_port=shipment_port
        self.paypal_payments_port=paypal_payments_port

    async def execute(self,order):
        try:
            # 1 Guardar orden interna
            order.payment_status = "PENDING"
            
            order_obtain=await self.order_port.save(order)  
            if not order_obtain:
                raise ValueError("No se pudo guardar la orden")
            
            my_uuuid=uuid.uuid4()
            now=datetime.now(timezone.utc)

            
            # 2 Crear la order
            
            paypal_order_create=await self.paypal_payments_port.create_order(
                order,reference_id=order_obtain["_id"])

            # 3 Actualizar el paypal order
            await self.order_port.update_paypal_order(order_obtain["_id"],paypal_order_create["id"])
            print("Orden creada",paypal_order_create)


            print("Save Order Guardada")            
            print("Realizando transporte",order_obtain)
            
            event={
                "estado":order.estado,
                "lugar":"New jersey",
                "fecha":now,
                "ubicacion_entrega":order.ubicacion,
                "created_at": now,
                "updated_at":now
            }
            
            shipment={
                "order_id":order_obtain["_id"],
                "transportista":"AWS",
                "numero_seguimiento":str(my_uuuid),
                "eventos":event,
                "firma":order.term_id,
                "estado":order.estado,
                "created_at":now,
                "updated_at":now
            }
            
            await self.shipment_port.save(shipment)
            
            #res_shipment=await self.shipment_port.save(shipment)
            #add_event=await self.shipment_port.add_event(
            #                res_shipment["_id"],event)  
            
            return {
            
                "status":"success",
                "order_id":order_obtain["_id"]
            }
         
        except Exception as e:
            return f"Ocurrio un error en execute order {e}"        

    async def capture_order_payment(self,paypal_order_id):
        try:
            order=await self.order_port.get_paypal_order_id(paypal_order_id)
            if not order:
                raise ValueError("No existe una orden asociada a Paypal")
            if order["payment_status"] == "COMPLETED":
                raise ValueError("Esta orden ya esta pagada")

            payment=await self.paypal_payments_port.capture(paypal_order_id)

            if payment["status"]!="COMPLETED":
                raise ValueError(f"El pago no se completo. Estado: {payment['status']}")

            if Decimal(str(order.monto)) != payment["amount"]:
                raise ValueError("El monto capturado no coincide con la orden")

            if order.currency != payment["currency"]:
                raise ValueError("La moneda capturada no coincide con la orden")

            await self.order_port.update_paypal_order(
                order._id,
                payment["capture_id"],
                payment["status"]
            )
            return {
                "status":"success",
                "capture_id":payment["capture_id"],
                "payment_status":payment["status"]
            }
        except Exception as e:
            return f"Error en capture_order_payment {e}"    
        