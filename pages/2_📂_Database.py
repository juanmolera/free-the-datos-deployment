# Streamlit
import streamlit as st

# Images
from PIL import Image

# Data manipulation
import pandas as pd

# Mongo database
import pymongo

# My functions
from src import api_get_cloud as ag

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Database', page_icon='📂')

# Title
st.markdown('# Database')
st.markdown('##### This is all the data you can download from this API. Any resemblance to real-world companies is mere coincidence.')

# Shows all databases
col1, col2, col3 = st.columns(3)

with col1:

    st.markdown('### Supermarket')
    #image = Image.open('images/diia.png')
    #st.image(image, use_column_width=True)

    st.markdown('### Second-hand cars')
    #image = Image.open('images/cnet.png')
    #st.image(image, use_column_width=True)

with col2:

    st.markdown('### Delivery')
    #image = Image.open('images/lovo.png')
    #st.image(image, use_column_width=True)

    st.markdown('### Tourist accommodation')
    #image = Image.open('images/arbib.png')
    #st.image(image, use_column_width=True)

with col3:

    st.markdown('### Real State')
    #image = Image.open('images/techno.png')
    #st.image(image, use_column_width=True)

    st.markdown('### Job offers')
    #image = Image.open('images/lin.png')
    #st.image(image, use_column_width=True)

# Availables databases to choose
# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()
db_availables = client.list_database_names()
db_availables.remove('admin')
db_availables.remove('config')
db_availables.remove('local')

# Chosen database
db_to_download = st.selectbox('Which database do you want to download?', ['Choose an option'] + db_availables)

if db_to_download in db_availables:

    # Chosen collection
    coll_availables = client[db_to_download].list_collection_names()

    coll_to_download = st.selectbox('Which collection do you want to download?', ['Choose an option'] + coll_availables)

    if coll_to_download in coll_availables:

        # Reads data to donwload
        data = ag.get_the_data(db_to_download, coll_to_download)
        df = pd.DataFrame.from_dict(data)
        df_normalized = pd.json_normalize(df[coll_to_download])
        csv_file = df_normalized.to_csv(index=False).encode('utf-8')
        json_file = df_normalized.to_json(orient = "records")

        st.markdown(f'#### Nice selection! You have chosen {coll_to_download}/{db_to_download} data. Please select a format:')

        # Download buttons
        st.download_button("Download csv", data=csv_file, file_name=f'free_the_data_API_{db_to_download}_{coll_to_download}.csv')
        st.download_button("Download json", data=json_file, file_name=f'free_the_data_API_{db_to_download}_{coll_to_download}.json')