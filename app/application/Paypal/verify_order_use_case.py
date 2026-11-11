from app.domain.ports.paypal_payment_gateway_port import PaypalPaymentGatewayPort

from app.domain.ports.order_port import OrderPort

from decimal import Decimal
from datetime import datetime,timezone


class PaypalVerifyOrderUseCase:

    def __init__(self,paypal_payment_port:PaypalPaymentGatewayPort,order_port:OrderPort):
        self.paypal_payment_port=paypal_payment_port
        self.order_port=order_port

    async def execute(self, order_id:str):

        order=await self.order_port.get(order_id)
        print("Order",order)
        if not order:
            raise ValueError("La orden no existe")
        
        paypal_capture_id = order.get("paypal_capture_id")
        
        if not paypal_capture_id:
            raise ValueError("La orden no tiene una captura asociada")

        # 2. Consultar captura directamente en PayPal

        payment= await self.paypal_payment_port.get_capture(paypal_capture_id)

        if not payment:
            raise ValueError("La captura no existe en paypal")

        # 3 verificar estado

        if payment.status!="COMPLETED":
            raise ValueError("El pago no esta completado")

        # 4 Verificar importe

        if payment.amount !=  Decimal(str(order["monto"])):
            raise ValueError("El importe de pago no coincide")

        # 5 verificar moneda

        if payment.currency != order["currency"]:
            raise ValueError("La moneda no coincide")

        return {
            "verified": True,
            "capture_id": payment.capture_id,
            "status": payment.status,
            "amount": str(payment.amount),
            "currency": payment.currency
        }