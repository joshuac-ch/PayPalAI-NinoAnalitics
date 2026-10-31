from abc import ABC,abstractmethod


class UserPort(ABC):

    @abstractmethod
    async def getUserID(self,user_id:int):
        pass
