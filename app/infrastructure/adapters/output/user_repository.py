
from app.domain.ports.user_port import UserPort
from app.infrastructure.adapters.output.connection import CreateConection 
from pymongo.errors import ConnectionFailure,ServerSelectionTimeoutError, PyMongoError 
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
class UserRepository(UserPort):

    def __init__(self,connection:CreateConection):
        self.collection_user=connection.get_collection(os.getenv("MONGO_TABLE_USER"))

    async def get(self, user_id):
        try:
            result= self.collection_user.find_one({"_id": ObjectId(user_id)})
            if result is None:
                return None
            result["_id"] = str(result["_id"])

            return result
        except ServerSelectionTimeoutError as e:
            print(f"Error: No se pudo encontrar o conectar al servidor MongoDB: {e}")   
        except ConnectionFailure as e:
            print(f"Error de conexión con MongoDB: {e}")
        except PyMongoError as e:
            print(f"Error general de PyMongo: {e}")        

    async def save(self, user):
        try:
            user_dict = user.model_dump()
            result = self.collection_user.insert_one(user_dict)
            return {
                "id": str(result.inserted_id),
                "success": True
            }
        except ServerSelectionTimeoutError as e:
            print(f"Error: No se pudo encontrar o conectar al servidor MongoDB: {e}")   
        except ConnectionFailure as e:
            print(f"Error de conexión con MongoDB: {e}")
        except PyMongoError as e:
            print(f"Error general de PyMongo: {e}")
                      