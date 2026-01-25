import streamlit as st

from sections.profile import show_Profile
from sections.projects import show_projects
from sections.skills import show_skills
from sections.contacts import show_contact

st.set_page_config(
    page_title="Abhay Sharma | ML Portfolio",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["Profile", "Projects", "Skills", "Contact"]
)

if page == "Profile":
    show_Profile()
    st.sidebar.success("Successfully reached to Profile Page!")

elif page == "Projects":
    show_projects()
    st.sidebar.success("Successfully reached to Projects Page!")

elif page == "Skills":
    show_skills()
    st.sidebar.success("Successfully reached to Skills Page!")

elif page == "Contact":
    show_contact()
    st.sidebar.success("Successfully reached to Contact Page!")

st.sidebar.divider()

st.sidebar.success("Portfolio Developed Using Streamlit!")


