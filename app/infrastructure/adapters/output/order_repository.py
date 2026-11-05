from app.domain.ports.order_port import OrderPort

class OrderRepository(OrderPort):

    def __init__(self):
        super().__init__()

    async def save(self, order):
        return await super().save(order)

    async def get(self, order_id):
        return await super().get(order_id)

    async def get_by_paypal_id(self, paypal_id):
        return await super().get_by_paypal_id(paypal_id)    