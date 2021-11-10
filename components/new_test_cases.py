import streamlit as st
import plotly.express as px
from utils.helpers import read_covid_data


def main():
    df = read_covid_data()
    df_countries = df[~df['iso_code'].str.contains('OWID')].dropna(subset=['new_cases', 'new_tests'])
    selected_country = st.selectbox(
        "Land",
        df_countries['location'].unique()
    )
    df_world_filtered = df_countries[df_countries['location'] == selected_country]
    fig = px.scatter(df_world_filtered,
                     x="new_tests",
                     y="new_cases",
                     trendline="ols",
                     trendline_color_override="red",
                     title="Aantal tests t.o.v. cases (lineair model)")
    fig.update_layout(xaxis_title="Aantal tests", yaxis_title="Aantal cases")
    st.plotly_chart(fig, use_container_width=True)
