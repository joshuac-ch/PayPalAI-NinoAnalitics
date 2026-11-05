from app.domain.ports.seller_police_port import SellerPolicePort

class SellerPoliceRepository(SellerPolicePort):

    def __init__(self):
        super().__init__()

    async def get_by_seller(self, seller_id):
        return await super().get_by_seller(seller_id)    


