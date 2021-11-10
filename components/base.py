import streamlit as st
from components.world_cases import main as world_cases_main
from components.income_classes import main as income_classes_main
from components.countries_cases import main as countries_cases_main
from components.map import main as map
from components.reproduction_rate import main as reproduction_rate_main
from components.new_test_cases import main as new_test_cases_main


def sidebar():
    st.sidebar.header('Dashboard setings')
    st.header("World COVID dashboard")

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

    world_cases_main()
    income_classes_main()
    countries_cases_main()
    map()
    reproduction_rate_main()
    new_test_cases_main()

    st.sidebar.markdown('[README.md](https://github.com/ItsMeSafak/youboard/blob/master/README.md)')

def main():
    sidebar()