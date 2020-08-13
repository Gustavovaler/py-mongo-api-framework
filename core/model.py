from database.connection import connect
from pymongo.collection import Collection

class Model:
    """
    self.db is an pymongo.connection instance
    """

    def __init__(self):
        self.db = connect()


    def set_collection(self, collection_name):
        self.collection = Collection(self.db,collection_name)

    def all(self):
        all_documents = [doc for doc in self.collection.find()]
        for document in all_documents:
            del document['_id']
        return all_documents

    def find_one(self, identifier):
        return identifier
        