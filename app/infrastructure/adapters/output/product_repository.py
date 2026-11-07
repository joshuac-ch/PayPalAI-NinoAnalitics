from app.domain.ports.product_port import ProductPort
from app.infrastructure.adapters.output.connection import CreateConection
import os
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId
from pymongo.errors import ServerSelectionTimeoutError,ConnectionFailure,PyMongoError
class ProductRepository(ProductPort):

    def __init__(self,connection:CreateConection):
        self.connection_product=connection.get_collection(os.getenv("MONGO_TABLE_PRODUCT"))

    async def save(self, product):
        try:
            serealizer= product.model_dump()
            await self.connection_product.insert_one(serealizer)
            return {
                "status":"success"
            }
        except ServerSelectionTimeoutError as e:
            print("No se pudo realiazr una conexcion con el servidor",e)    
        except ConnectionFailure as e:
            print("Ocurrio un error con la conexion",e)
        except PyMongoError as e:
            print("Ocurrio un error general en pymongo",e)

    async def get(self, product_id):
        try:
            result=await self.connection_product.find_one({"_id":ObjectId(product_id)})
            if result is None:
                return None
            result["_id"]=str(result["_id"])
            
            return result
        except ServerSelectionTimeoutError as e:
            print("No se pudo realiazr una conexcion con el servidor",e)    
        except ConnectionFailure as e:
            print("Ocurrio un error con la conexion",e)
        except PyMongoError as e:
            print("Ocurrio un error general en pymongo",e)
        

    async def list_product(self):
        try:
            cursor=self.connection_product.find()
            products= await cursor.to_list()
            for product in products:
                product["_id"] = str(product["_id"])
            return products
        except ServerSelectionTimeoutError as e:
            print("No se pudo realiazr una conexcion con el servidor",e)    
        except ConnectionFailure as e:
            print("Ocurrio un error con la conexion",e)
        except PyMongoError as e:
            print("Ocurrio un error general en pymongo",e)
         