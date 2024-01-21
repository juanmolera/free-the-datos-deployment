# Streamlit
import streamlit as st

# Images
from PIL import Image

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Contact', page_icon='💌')

col1, col2, col3 = st.columns(3)

with col1:

    pass

with col2:


    image = Image.open('images/roberto_capucha.png')
    st.image(image, use_column_width=True)
    st.markdown('<a href="mailto:juan.molera@gmail.com">Mail me!</a>', unsafe_allow_html=True)
    

with col3:

    pass