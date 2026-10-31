
from app.domain.ports.user_port import UserPort
from app.infrastructure.adapters.output.connection import CreateConection 
import os
from dotenv import load_dotenv
load_dotenv()
class UserRepository(UserPort):

    def __init__(self,connection:CreateConection):
        self.collection_user=connection.get_collection(os.getenv("MONGO_TABLE_USER"))
        self.collection_conrversations=connection.get_collection(os.getenv("MONGO_TABLE_MODEL"))
        
    async def getUserID(self, user_id:int):
        user = self.collection_conrversations.find_one({"_id": user_id})
        return user