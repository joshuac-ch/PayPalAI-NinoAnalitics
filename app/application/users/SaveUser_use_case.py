
from app.domain.ports.user_port import UserPort
class SaveUserUseCase():
    def __init__(self,user_port:UserPort):
        self.user_port=user_port

    async def create_user(self,user):
        try:
            return await self.user_port.save(user)
        except Exception as e:
            return {"Error": f"Ocurrio un error {e}"}    