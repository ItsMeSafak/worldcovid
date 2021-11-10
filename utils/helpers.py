import streamlit as st
import pandas as pd

URL = "data/owid-covid-data.csv"


@st.cache
def read_covid_data():
    return pd.read_csv(URL, parse_dates=['date'])
