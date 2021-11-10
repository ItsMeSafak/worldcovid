import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_income = df[df['location'].str.contains('income')]

    fig = px.scatter(df_income,
                     x='date',
                     y='total_cases',
                     title='Total cases per income class',
                     color='location',
                     hover_data=['location'])
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(df_income,
                     x='date',
                     y='total_deaths',
                     title='Total deaths per income class',
                     color='location',
                     hover_data=['location'])
    st.plotly_chart(fig, use_container_width=True)
