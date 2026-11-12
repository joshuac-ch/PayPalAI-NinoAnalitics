from abc import abstractmethod, ABC
from app.domain.entities.Dispute import Dispute
from app.domain.entities.Offer import Offer
from app.domain.entities.Evidence import Evidence 
# Disputas con ofertas y evidencias 
class DisputePort(ABC):

    @abstractmethod
    async def get(self,dispute_id:str) -> Dispute | None:
        pass

    @abstractmethod 
    async def get_by_paypal_id(self,paypal_id:str) -> Dispute | None:
        pass

    @abstractmethod    
    async def save(self,dispute:Dispute) -> None:
        pass 
    
    @abstractmethod
    async def list_open(self,seller_id:str | None = None) -> list[Dispute]:
        pass

    @abstractmethod
    async def list_seller(self,seller_id:str) -> list[Dispute]:
        pass 

    @abstractmethod
    async def add_offer(self, dispute_id: str, offer: Offer):
        pass

    @abstractmethod
    async def add_evidence(self, dispute_id: str, evidence: Evidence):
        pass   
