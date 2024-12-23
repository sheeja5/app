import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=False,
)
project_1_page = st.Page(
    "Nyaysathi.py",
    title="Sales Dashboard",
    icon=":material/balance:",
    default=True,
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

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
