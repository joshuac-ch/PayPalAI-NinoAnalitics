from app.domain.ports.term_port import TermPort
from app.infrastructure.adapters.output.connection import CreateConection
from dotenv import load_dotenv
import os
from bson import ObjectId
from pymongo.errors import PyMongoError,ConnectionFailure,ServerSelectionTimeoutError
load_dotenv()
class TermRepository(TermPort):

    def __init__(self,connection:CreateConection):
        self.connection_term=connection.get_collection(os.getenv('MONGO_TABLE_TERM'))

    async def get(self, term_id):
        try:
            term=await self.connection_term.find_one({"_id":ObjectId(term_id)})
            if term is None:
                return None
            term["_id"]=str(term["_id"])
            return term
        except ServerSelectionTimeoutError as e:
            print(f"Error: No se pudo encontrar o conectar al servidor MongoDB: {e}")   
        except ConnectionFailure as e:
            print(f"Error de conexión con MongoDB: {e}")
        except PyMongoError as e:
            print(f"Error general de PyMongo: {e}")    
    
    async def save(self, term):
        try:
            term_save=term.model_dump()
            await self.connection_term.insert_one(term_save)
            return {
                "status":"sucess"
            }    
        except ServerSelectionTimeoutError as e:
            print(f"Error: No se pudo encontrar o conectar al servidor MongoDB: {e}")   
        except ConnectionFailure as e:
            print(f"Error de conexión con MongoDB: {e}")
        except PyMongoError as e:
            print(f"Error general de PyMongo: {e}")       


    
        