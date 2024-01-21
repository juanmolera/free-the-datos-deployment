# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# MongoDB
import pymongo

# My functions
from src import quickie_functions as quick
from src import api_get_cloud as ag

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Quickie', page_icon='🔮')

# Title
st.markdown('# Quickie')

# Availables databases to choose
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()
db_availables = client.list_database_names()
db_availables.remove('admin')
db_availables.remove('config')
db_availables.remove('local')

# Chosen database
db_to_explore = st.selectbox('Which database do you want to explore?', ['Choose an option'] + db_availables)

if db_to_explore in db_availables:

    coll_availables = client[db_to_explore].list_collection_names()

    # Chosen collection
    coll_to_download = st.selectbox('Which collection do you want to explore?', ['Choose an option'] + coll_availables)

    if coll_to_download in coll_availables:

        # Reads data to explore
        data = ag.get_the_data(db_to_explore, coll_to_download)
        df = pd.DataFrame.from_dict(data)
        df_normalized = pd.json_normalize(df[coll_to_download])

        # Shows EDA
        quick.eda(df_normalized)