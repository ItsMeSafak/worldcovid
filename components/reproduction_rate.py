import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_world = df[df['location'] == 'World'].sort_values('date')
    df_world['monthyear'] = df_world.date.dt.strftime('%B %Y')

    selected_monthyear = st.selectbox(
        "Maand & Jaar",
        df_world['monthyear'].unique()
    )

    df_world_filtered = df_world[df_world['monthyear'] == selected_monthyear]

    fig = px.box(df_world_filtered, y="reproduction_rate")
    st.plotly_chart(fig)
