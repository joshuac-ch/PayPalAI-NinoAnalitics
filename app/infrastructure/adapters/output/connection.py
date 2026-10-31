from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class CreateConection():
    _insinstance=None

    def __new__(cls):
        if cls._insinstance is None:
            cls._insinstance=super(CreateConection,cls).__new__(cls)
            # Una sola vez
            cls._insinstance.client= MongoClient(os.getenv("MONGO_URL"))
            cls._insinstance.db=cls._insinstance.client[os.getenv("MONGO_DB")]
            print("Collecions creadas exitosamente")
        return cls._insinstance

    def get_collection(self,collection_name:str):
        return self.db[collection_name]
   

 