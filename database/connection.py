from pymongo import MongoClient
from config.config  import db_host, db_port, db_name

client = MongoClient(db_host, db_port)

db = client[db_name]




