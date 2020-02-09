import pandas as pd
from lib import mongo, handler


def ingest_excel(file):
    pass

def ingest_csv(file):
    pass

class run(object):
    def __init__(self, arguments, system):
        self.__args = arguments
        self.__system = system
        self.__debug = False if not self.__args.debug else self.__args.debug
        self.run()

    def run(self):
        print (self.__args)

    def intgest(self):
        print ("Running Ingest")

        # Check if file exists before reading
        if not handler.checkFile(self.__args.file):
            return False

        # Based on file type read the csv
        # Convert csv dictionary to JSON
        # Insert many to MongoDb
