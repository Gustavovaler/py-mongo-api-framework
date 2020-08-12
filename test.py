import unittest
import pymongo
from database import connection
from database.migrations import migrations

class TestApplication(unittest.TestCase):

    def test_db_conn(self):
        self.assertIsInstance(connection.connect(),pymongo.database.Database)

        

if __name__=="__main__":
    unittest.main()