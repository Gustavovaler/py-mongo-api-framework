from database.connection import db

class Model:

    """
    self.db is an pymongo.connection instance
    """

    def __init__(self):
        self.db = db