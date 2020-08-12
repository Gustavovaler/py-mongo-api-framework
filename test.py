import unittest
import pymongo
from aiohttp import web
from core.model import Model
from core.app import app
from database import connection
from database.migrations import migrations


class TestApplication(unittest.TestCase):

    def test_aiphttp_app(self):
        self.assertIsInstance(app, web.Application)

    def test_db_conn(self):
        self.assertIsInstance(connection.connect(),pymongo.database.Database)

    def test_model_class(self):
        self.assertIsInstance(Model(), Model)


if __name__=="__main__":
    unittest.main()