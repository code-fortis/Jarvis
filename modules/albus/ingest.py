# Import Pandas
import pandas as pd

# Import handler and mongo from library
from lib import handler, mongo

def ingest_csv(filename=None, db=None, collection=None):
    # Return False if any of the required arguments are None
    if not filename.strip() or not db.strip() or not collection.strip():
        return False
    
    # Connect to MongoDatabase

    # Read CSV via pandas
    try:
        csv_data =  pd.read_csv(filename)
    except Exception as error:
        print ("Error: \n{}".format(str(error)))
        return False

