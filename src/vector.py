import streamlit as st
from streamlit_option_menu import option_menu

st.markdown(
    """
    <style>
    .main.block-container{
        padding:0;
        background-color:green;
    }
    """,
    unsafe_allow_html=True,
)
st.title("Maxon Dashboards")

# with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=["Home", "Dashboards", "Contact"],
    icons=["house", "book", "envelope"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.write(f"Welcome to the Maxon")
if selected == "Dashboards":
    st.write(f"Dashboars")
if selected == "Contact":
    st.write(f"Contact us")
