import streamlit as st

def sidebar():
    st.sidebar.header('Dashboard setings')
    st.header("World COVID dashboard")

    pages = {
        "Map": components.laadpalen,
        "1D Inspecties": components.ocm,
        "2D Inspecties": components.rdw,
        "Lineair model": components.rdw
    }
    st.sidebar.title("Navigatie")
    select = st.sidebar.selectbox(
        "Pagina",
        pages.keys()
    )
    pages[select].main()

    st.sidebar.markdown('[README.md](https://github.com/ItsMeSafak/youboard/blob/master/README.md)')

def main():
    sidebar()