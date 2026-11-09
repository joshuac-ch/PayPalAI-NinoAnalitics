from app.domain.ports.dispute_port import DisputePort
from app.infrastructure.adapters.output.connection import CreateConection

from pymongo.errors import PyMongoError,ConnectionFailure,ServerSelectionTimeoutError
from dotenv import load_dotenv
import os
from bson import ObjectId

class DisputeRepository(DisputePort):

    def __init__(self,connection:CreateConection):
        self.collection_dispute=connection.get_collection(os.getenv('MONGO_TABLE_DISPUTE'))

    async def get(self, dispute_id):
        try:

            result=await self.collection_dispute.find_one({"_id":ObjectId(dispute_id
            )})
            
            if result is None:
                return None
            result["_id"]=str(result["_id"])
            return result

        except ConnectionFailure as e:
            return f"Errro de conection fallida {e}"    
        except ServerSelectionTimeoutError as e:
            return f"Error en el tiempo de connexion {e}"    
        except PyMongoError as e:
            return f"Error general de pymongo {e}"              

    async def get_by_paypal_id(self, paypal_id):
        return await super().get_by_paypal_id(paypal_id)

    async def save(self, dispute):
        try:
            dispute_dict=dispute.model_dump()
            
            create_dispute=await self.collection_dispute.insert_one(dispute_dict)

            return {
                "status":"success"
            }
        except ConnectionFailure as e:
            return f"Errro de conection fallida {e}"    
        except ServerSelectionTimeoutError as e:
            return f"Error en el tiempo de connexion {e}"    
        except PyMongoError as e:
            return f"Error general de pymongo {e}"    

    async def list_open(self, seller_id = None):
        return await super().list_open(seller_id)

    async def list_seller(self, seller_id):
        return await super().list_seller(seller_id)
        