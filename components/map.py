import plotly.express as px
import streamlit as st
from utils.helpers import read_covid_data, read_geo_data
from datetime import date

def main():
    df_covid = read_covid_data()
    df_geo = read_geo_data()
    start_h, end_h = (date(2020, 2, 24), date(2021, 11, 11))
    start_h, end_h = st.slider("Selecteer een periode", start_h, end_h,
                                        (start_h, end_h), key="Globalslider")

    df_covid = df_covid.loc[(df_covid['date']>str(start_h)) & (df_covid['date']<str(end_h))]

    df = df_covid.groupby(['location', 'iso_code']).sum().reset_index()
    df = df.merge(df_geo, left_on='iso_code', right_on='ISO_A3')
    geo = df_geo.set_index('ISO_A3')
    fig = px.choropleth_mapbox(df, geojson=geo, locations=df['iso_code'], color='new_cases',
                                color_continuous_scale="Viridis",
                                mapbox_style="carto-positron",
                                range_color=(0, df['new_cases'].mean()),
                                opacity=0.5,
                                zoom=1)
    fig.update_layout(title="Totaal aantal cases over de wereld", coloraxis_colorbar={ 
        "title":"Totaal cases"})
    st.plotly_chart(fig, use_container_width=True)