from database.connection import connect

class Model:
    """
    self.db is an pymongo.connection instance
    """

    def __init__(self):
        self.db = connect()
        