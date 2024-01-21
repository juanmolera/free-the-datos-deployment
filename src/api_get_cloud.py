import pymongo
from fastapi import FastAPI
import pandas as pd
import streamlit as st

def get_the_data(database, collection):

    # Initialize connection.
    # Uses st.cache_resource to only run once.
    @st.cache_resource
    def init_connection():
        return pymongo.MongoClient(**st.secrets["mongo"])

    client = init_connection()

    # Pull data from the collection.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
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
