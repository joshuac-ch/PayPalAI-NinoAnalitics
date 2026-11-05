from app.domain.ports.paypal_payment_gateway_port import PaypalPaymentGatewayPort

class PaypalPaymentGateway(PaypalPaymentGatewayPort):

    def __init__(self):
        super().__init__()

    async def create_order(self, order):
        return await super().create_order(order)

    async def capture(self, paypal_order_id):
        return await super().capture(paypal_order_id)

    async def get_order(self, paypal_order_id):
        return await super().get_order(paypal_order_id)
    