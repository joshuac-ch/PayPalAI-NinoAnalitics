from app.domain.ports.paypal_dispute_gateway_port import PaypalDisputeGatewayPort

class PaypalDisputeUseCase:

    def __init__(self,paypal_dispute_port:PaypalDisputeGatewayPort):
        self.paypal_dispute_port=paypal_dispute_port

    async def execute(self,paypal_dispute_id):
        try:
            return await paypal_dispute_id
        except Exception as e:
            return f"Error PaypalDisputeUseCase {e}"        