
from app.domain.ports.user_port import UserPort

class GetUsersUseCase:

    def __init__(self,user_port:UserPort):
        self.user_port=user_port

    async def find_user_id(self,id:int):        
        return await self.user_port.getUserID(id)
