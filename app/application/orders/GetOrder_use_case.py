from app.domain.ports.order_port import OrderPort

class GetOrderUseCase:

    def __init__(self,order_port:OrderPort):
        self.order_port=order_port

     
