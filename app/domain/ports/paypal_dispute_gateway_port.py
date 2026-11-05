from abc import abstractmethod,ABC


class PaypalDisputeGatewayPort(ABC):

    @abstractmethod
    async def get_dispute(self,dispute_id):
        pass

    @abstractmethod    
    async def send_message(self,message):
        pass

    @abstractmethod
    async def make_offer(self):
        pass

    @abstractmethod
    async def provide_evidence(self):
        pass

    @abstractmethod
    async def accept_claim(self):
        pass 

    @abstractmethod
    async def escalate(self):
        pass    