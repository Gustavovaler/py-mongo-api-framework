from pymongo import MongoClient
from config.config  import DB_HOST, DB_NAME, DB_PORT

client = MongoClient(DB_HOST, DB_PORT)

db = client[DB_NAME]




