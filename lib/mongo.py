# Import all the modules required
import pymongo

# import logging function
from . import logger
log = logger.log

class mongo(object):
    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
    
    def connect(self, username=None, password=None):
        ''' Connect to Mongo Database '''
        self.client = pymongo.MongoClient(self.host, self.port, username=username, password=password)
        if not self.client:
            return False
        return True
    
    def get_db(self, database=None):
        if not database:
            return False
        # Check if database exists or not
        db = self.client[database]
        if db:
            return False
        return db

    def check_db(self, database=None):
        return False if not database or database not in self.client.list_database_names() else True

    def check_collection(self, database=None, collection=None):
        if not database or not collection:
             return False

        if self.check_db(database=database):
            db = self.get_db(database=database)
            return False if not db or collection not in db.collection_names() else True
