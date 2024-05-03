from pymongo import MongoClient
from warehouse import settings
import json
import pandas

DB_NAME = settings.DATABASES.get("default").get("NAME")
DB_HOST = settings.DATABASES.get("default").get("CLIENT").get("host")
DB_PORT = settings.DATABASES.get("default").get("CLIENT").get("port")

def mongoimport(csv_path, col_name, db_name=DB_NAME, db_url=DB_HOST, db_port=DB_PORT):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: new collection
    """
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    collection = db[col_name]
    data = pandas.read_csv(csv_path)
    data_json = json.loads(data.to_json(orient='records'))
    # collection.remove()
    result = collection.insert(data_json)
    return collection

if __name__ == "__main__":
    mongoimport("././statics/data/data.csv", "seed")