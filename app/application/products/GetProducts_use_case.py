from app.domain.ports.product_port import ProductPort


class GetProductsUseCase:

    def __init__(self,product_port:ProductPort):
        self.product_port=product_port

    async def get_product(self,product_id):
        try:
            return await self.product_port.get(product_id)
        except Exception as e:
            print("Ocurrio un erro en get_product: ",e)    

    async def list_product(self):
        try:
            return await self.product_port.list_product()
        except Exception as e:
            print("Ocurrio un errro en list_product: ",e)    
