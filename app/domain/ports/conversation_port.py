from abc import abstractmethod,ABC
from app.domain.entities.Conversation import Conversation
from app.domain.entities.Message import Message
# chats comprador, vendedor y mediador 
class ConversationPort(ABC):

    @abstractmethod
    async def create(self,conversation:Conversation) -> None:
        pass

    @abstractmethod
    async def get_by_dispute(self,dispute_id:str) -> Conversation | None:
        pass    

    @abstractmethod    
    async def add_message(self,conversation_id:str,message:Message) -> None:
        pass
