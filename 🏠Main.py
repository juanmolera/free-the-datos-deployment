# Streamlit
import streamlit as st

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Main', page_icon='🏠')

# CSS access
with open('css/style2.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True)

st.markdown('# Data Analytics Bootcamp')
st.markdown('## Final project: Free the data API')
st.markdown('## Juan Molera Pascual')
st.markdown('#### October 2023')
st.markdown('##### Ironhack')
