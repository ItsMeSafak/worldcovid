import streamlit as st

def sidebar():
    # Global variables to check on plots
    global showPlots
    global showCode
    global start_h
    global end_h

    st.sidebar.header('Dashboard setings')
    st.header("Youboard")

    # start_h, end_h = (date(1970, 2, 1), date.today())

    # pages = {
    #     "Alles": components.landingpage,
    #     "Laadpalen": components.laadpalen,
    #     "Open charge map": components.ocm,
    #     "RDW Data": components.rdw
    # }
    # st.sidebar.title("Navigatie")
    # select = st.sidebar.selectbox(
    #     "Pagina",
    #     pages.keys()
    # )

    # if (select == "RDW Data" or select == "Alles"):
    #     # Date selector
    #     st.sidebar.header("Selecteer een start en eind datum:")
    #     start_h = st.sidebar.date_input('Start datum', start_h, key = "startd")
    #     end_h = st.sidebar.date_input('Eind datum', end_h, key = "endd")

    #     # Slider for date
    #     start_h, end_h = st.sidebar.slider("Selecteer een periode", start_h, end_h,
    #                                     (start_h, end_h), key="Globalslider")
    
    # pages[select].main()

    st.sidebar.markdown('[README.md](https://github.com/ItsMeSafak/youboard/blob/master/README.md)')

def main():
    sidebar()