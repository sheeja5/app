import streamlit as st
from streamlit_option_menu import option_menu


about_page = st.Page(
       "about_me.py",
        title="About",
        icon=":material/info:",
        default=True,
    )
project_1_page = st.Page(
        "Nyaysathi.py",
        title="Nyaysathi",
        icon=":material/balance:",
)

# --- PAGE SETUP ---
nyaysathi = (":material/balance:")
selection = option_menu(
    menu_title = "Main Menu",
    options = ["About","Nyaysathi"],
    icons = ["info",nyaysathi],
    orientation = "horizontal",
)
if selection == "About":
    open (about_me.py)   
#if selection == "Nyaysathi":
 


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, project_1_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
       "Info": [about_page],
      "Projects": [project_1_page],
    }
)


# --- SHARED ON ALL PAGES ---
#st.logo("assets/codingisfun_logo.png")
#st.sidebar.markdown("Made with ❤️ by [Sven](https://youtube.com/@codingisfun)")


# --- RUN NAVIGATION ---
pg.run()
