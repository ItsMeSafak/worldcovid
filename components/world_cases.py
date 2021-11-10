import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_world = df[df['location'] == 'World']

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(
        go.Scatter(x=df_world['date'], y=df_world['total_cases'], name='Total Cases'),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df_world['date'], y=df_world['total_deaths'], name='Total Deaths'),
        secondary_y=True
    )
    fig.update_layout(title_text='Total cases/deaths in the world')
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Case count in Millions", secondary_y=False)
    fig.update_yaxes(title_text="Death count in Millions", secondary_y=True)

    st.plotly_chart(fig)
