import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_countries = df[~df['iso_code'].str.contains('OWID')]

    fig = px.scatter(df_countries,
                     x='date',
                     y='total_cases',
                     title='Totaal aantal cases per land',
                     trendline='ols',
                     trendline_color_override='red',
                     hover_data=['location'],
                     labels={
                         "date": "Datum",
                         "total_cases": "Totaal aantal cases",
                         "location": "Locatie"
                     })
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(df_countries,
                     x='date',
                     y='total_deaths',
                     title='Totaal aantal sterfgevallen per land',
                     trendline='ols',
                     trendline_color_override='red',
                     hover_data=['location'],
                     labels={
                         "date": "Datum",
                         "total_deaths": "Totaal aantal sterfgevallen",
                         "location": "Locatie"
                     })
    st.plotly_chart(fig, use_container_width=True)
