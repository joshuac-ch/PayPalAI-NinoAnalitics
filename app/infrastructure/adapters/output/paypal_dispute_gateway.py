from app.domain.ports.paypal_dispute_gateway_port import PaypalDisputeGatewayPort

class PaypalDisputeGateway(PaypalDisputeGatewayPort):

    def __init__(self):
        super().__init__()

    async def get_dispute(self, dispute_id):
        return await super().get_dispute(dispute_id)

    async def send_message(self, message):
        return await super().send_message(message)

    async def make_offer(self):
        return await super().make_offer()

    async def provide_evidence(self):
        return await super().provide_evidence()

    async def accept_claim(self):
        return await super().accept_claim()

    async def escalate(self):
        return await super().escalate()
        