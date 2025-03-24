import streamlit as st
from streamlit_option_menu import option_menu

about_page = st.Page(
    "about_me.py",
    title="About",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "nyaysathi.py",
    title="Nyaysathi",
    icon=":material/balance:",
    default=False,
)
project_2_page = st.page(
    "complaint_generator.py",
    title= " Complaint Generator",
    icon= ":material/balance:",
    default= False,
)    

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
        "Projects": [project_2_page],
        
    }
)


# --- SHARED ON ALL PAGES ---
#st.logo("assets/codingisfun_logo.png")
#st.sidebar.markdown("Made with ❤️ by [Sven](https://youtube.com/@codingisfun)")


# --- RUN NAVIGATION ---
pg.run()
