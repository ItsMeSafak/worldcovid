import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from utils.helpers import read_covid_data


def barplot():
    df = read_covid_data()
    df = df.groupby(['location', 'iso_code']).sum().reset_index()
    df_top_10 = df.sort_values('new_cases', ascending=False)[:10]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_top_10['new_cases'],
                    y=df_top_10['location'],
                    name='Totaal cases',
                    orientation='h'
                    ))
    fig.add_trace(go.Bar(x=df_top_10['new_deaths'],
                    y=df_top_10['location'],
                    name='Aantal doden',
                    orientation='h'
                    ))
    fig.update_layout(title="Aantal doden en aantal corona gevallen")
    st.plotly_chart(fig, use_container_width=True)

def lineplot():
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

def main():
    barplot()
    lineplot()