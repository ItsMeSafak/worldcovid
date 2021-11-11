import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_income = df[df['location'].str.contains('income')]

    fig = px.line(df_income,
                  x='date',
                  y='total_cases',
                  title='Totaal aantal cases per inkomsten klassen',
                  color='location',
                  hover_data=['location'],
                  labels={
                      "date": "Datum",
                      "total_cases": "Totaal aantal cases",
                      "location": "Locatie",
                  })
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(df_income,
                  x='date',
                  y='total_deaths',
                  title='Totaal aantal sterfgevallen per inkomsten klassen',
                  color='location',
                  hover_data=['location'],
                  labels={
                      "date": "Datum",
                      "total_deaths": "Totaal aantal sterfgevallen",
                      "location": "Locatie",
                  })
    st.plotly_chart(fig, use_container_width=True)
