from database.connection import connect
from pymongo.collection import Collection
from bson import BSON
from bson import json_util
import json
from pymongo.collection import ObjectId


class Model:
    """
    self.db is an pymongo.connection instance
    """

    def __init__(self):
        self.db = connect()


    def normalize_id(self, all_documents):        
        for document in all_documents:
            document['id'] = json.dumps(document['_id'], default=json_util.default)
            del document['_id']
            document['id']=json.loads(document['id'])['$oid']
        return all_documents

    def set_collection(self, collection_name):
        self.collection = Collection(self.db,collection_name)

    def all(self):   # controller.index
        all_documents = [doc for doc in self.collection.find()]
        docs = self.normalize_id(all_documents)
        return docs

    def find_one(self, identifier):  #  controller.show
        try :
            if identifier['id']:
               result = self.collection.find_one({'_id':ObjectId(identifier['id'])})
               if result == None:
                    return None
               result = self.normalize_id([result])
               return result[0]
        except:
            if len(identifier) == 1 :        
                result = self.collection.find_one(identifier)
                if result == None:
                    return None
                result = self.normalize_id([result])
                return result[0]
    
    def insert_one(self,document):
        res = self.collection.insert_one(document)
        return res

    def delete_one(self, identifier):
        try :
            if identifier['id']:
               result = self.collection.delete_one({'_id':ObjectId(identifier['id'])})
               if result == None:
                    return None
               result = self.normalize_id([result])
               return result[0]
        except:
            if len(identifier) == 1 :        
                result = self.collection.delete_one(identifier)
                if result == None:
                    return None 

                return True
    