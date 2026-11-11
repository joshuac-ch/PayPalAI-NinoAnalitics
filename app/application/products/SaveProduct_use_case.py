
from app.domain.ports.product_port import ProductPort
class SaveProductUseCase:

    def __init__(self,product_port:ProductPort):
        self.product_port=product_port


    async def create_product(self,product):
        try:
            return await self.product_port.save(product)
        except Exception as e:
            print("Ocurri un errro en create product ",e)    