import streamlit as st
from components import base


st.set_page_config(
        page_title='World Covid',
        layout='wide',
        initial_sidebar_state="expanded"
    )

if __name__ == "__main__":
    base.main()