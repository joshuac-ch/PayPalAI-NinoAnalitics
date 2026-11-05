from app.domain.ports.shipment_port import ShipmentPort

class ShipmentRepository(ShipmentPort):

    def __init__(self):
        super().__init__()

    async def get_by_order(self, order_id):
        return await super().get_by_order(order_id)

    async def add_event(self, event):
        return await super().add_event(event)    