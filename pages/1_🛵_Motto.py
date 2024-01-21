# Streamlit
import streamlit as st

# Images
from PIL import Image

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Motto', page_icon='🛵')

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    pass

with col2:

    st.markdown('# Free the data API')
    image = Image.open('images/free.png')
    st.image(image, use_column_width=True)
    st.markdown("#### Imagine a world where you don't have to do data projects on the titanic, publications, weather or diamonds. You're welcome.")
    

with col3:

    pass