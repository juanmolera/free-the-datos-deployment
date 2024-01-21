import pymongo
from fastapi import FastAPI
import pandas as pd

client = pymongo.MongoClient('mongodb://localhost:27017/')

def get_the_data(database, collection):

    db = client[database]
    coll = db[collection]
    df = pd.DataFrame(list(coll.find()))
    del df['_id']

    data = df.to_dict(orient = "records")

    app = FastAPI()

    @app.get(f'/{database}/{collection}')
    def get_collection():
        return {f'{collection}': data}
    
    return get_collection()