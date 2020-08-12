from pymongo import MongoClient
from config.config  import DB_HOST, DB_NAME, DB_PORT


def connect():
    try:      
        client = MongoClient(DB_HOST, DB_PORT)
        db = client[DB_NAME]
        if db:
            
            return db
    except:
        return "Error de conexion a la base de  datos"


