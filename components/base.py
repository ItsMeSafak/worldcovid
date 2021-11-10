import streamlit as st
from components.world_cases import main as world_cases_main
from components.income_classes import main as income_classes_main
from components.countries_cases import main as countries_cases_main
from components.map import main as map
from components.reproduction_rate import main as reproduction_rate_main
from components.new_test_cases import main as new_test_cases_main
from components.barplot import main as barplot


def sidebar():
    st.sidebar.header('Dashboard setings')
    st.header("World COVID dashboard")
    st.markdown("*Welkom bij de World COVID dashboard. U bevindt zich op de landingspagina waarin een introductie wordt toegelicht met het gebruik van de data. Links aan de sidebar staat er een dropdown waarbij u kunt navigeren naar de verschillende data inspecties in deze dashboard. Onderaan de sidebar is er ook een link naar een [README.md](https://github.com/ItsMeSafak/youboard/blob/master/README.md) bestand. Hier staat de technische deel van de documentatie.*")
    st.header("Data gebruik")
    st.subheader("OWID COVID Data")
    st.markdown("*Referenties: https://ourworldindata.org/coronavirus#coronavirus-country-profiles *")
    st.markdown("*De dataset die wij hebben gebruikt in deze dashboard is afkomstig van 'Our World in Data' waaruit we een CSV bestand hebben opgehaald. Deze csv bestaat uit alle data over corona over heel de wereld. Al zijn het nieuwe cases, oude cases, aantal geteste, bevolking en nog veel meer. Wij hebben voornamelijk gefocussed op de bevestigde cases over heel de wereld, het reprodcutie getal en het aantal doden.*")
    st.subheader("Countries GEOJson")
    st.markdown("*Referenties: https://github.com/johan/world.geo.json/blob/master/countries.geo.json *")
    st.markdown("*Ook hebben we de countries geojson gebruikt, waarin geospatiale in verwerkt staat over heel de wereld. Deze dataset hebben wij gebruikt als een hulpmiddel voor de OWID Covid dataset. Dankzij de polygons die verwerkt staan in deze dataset hebben we de datasets gemerged op ISO code (bijvoorbeeld AUS = Australie) en zo hebben we geospatiale inspectie kunnen uitvoeren op de dataset.*")

    pages = {
        "Map": "",
        "1D Inspecties": "",
        "2D Inspecties": "",
        "Lineair model": ""
    }
    st.sidebar.title("Navigatie")
    select = st.sidebar.selectbox(
        "Pagina",
        pages.keys()
    )
    # pages[select].main()

    barplot()
    world_cases_main()
    income_classes_main()
    countries_cases_main()
    map()
    reproduction_rate_main()
    new_test_cases_main()

    st.sidebar.markdown('[README.md](https://github.com/ItsMeSafak/youboard/blob/master/README.md)')

def main():
    sidebar()