import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_countries = df[~df['iso_code'].str.contains('OWID')]

    fig = px.scatter(df_countries,
                     x='date',
                     y='total_cases',
                     title='Total cases per country',
                     trendline='ols',
                     trendline_color_override='red',
                     hover_data=['location'])
    st.plotly_chart(fig)

    fig = px.scatter(df_countries,
                     x='date',
                     y='total_deaths',
                     title='Total deaths per country',
                     trendline='ols',
                     trendline_color_override='red',
                     hover_data=['location'])
    st.plotly_chart(fig)
