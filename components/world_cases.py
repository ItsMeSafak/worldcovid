import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_world = df[df['location'] == 'World']

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(
        go.Scatter(x=df_world['date'],
                   y=df_world['total_cases'],
                   name='Totaal aantal cases'),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df_world['date'],
                   y=df_world['total_deaths'],
                   name='Totaal aantal sterfgevallen'),
        secondary_y=True
    )
    fig.update_layout(title_text='Totaal aantal cases/sterfgevallen in de wereld')
    fig.update_xaxes(title_text="Datum")
    fig.update_yaxes(title_text="Cases in Miljoenen", secondary_y=False)
    fig.update_yaxes(title_text="Sterfgevallen in Miljoenen", secondary_y=True)

    st.plotly_chart(fig, use_container_width=True)
