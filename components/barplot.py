import plotly.graph_objects as go
import streamlit as st
from utils.helpers import read_covid_data


def main():
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