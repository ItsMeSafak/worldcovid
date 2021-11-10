import streamlit as st
import pandas as pd
import geopandas as gpd
from datetime import date

URL_COVID = "data/owid-covid-data.csv"
URL_GEO = "data/countries.geojson"

@st.cache
def read_covid_data():
    return pd.read_csv(URL_COVID, parse_dates=['date'])

@st.cache
def read_geo_data():
    return gpd.read_file(URL_GEO)
