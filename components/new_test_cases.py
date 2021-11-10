import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_countries = df[~df['iso_code'].str.contains('OWID')]
    fig = px.scatter(df_countries,
                     x="new_tests",
                     y="new_cases",
                     trendline="ols",
                     trendline_color_override="red")
    st.plotly_chart(fig)
