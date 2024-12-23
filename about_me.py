import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Icon for title
icon1 = ":material/description:"
# Content of the introduction
col1,col2 = st.columns(2, gap ="small", vertical_alignment ="center")
with col1:
  st.title(f"Introduction {icon1}")
with col2:
  st.image("Screenshot (2).png", width=230)
st.markdown("## **Nyaysathi**")
c1,c2 = st.columns(2, gap="small", vertical_alignment="center")
with c1:
  st.image("DALL·E 2024-12-23 18.56.53 - A highly realistic and emotional illustration showing poor people living on the streets of India, with a backdrop of crowded streets and humble shelte.webp", width=230)
with c2:
  st.markdown("""NyaySathi: A perfect legal Assistant

  **Imagine you’re in a situation where someone refuses to return your hard-earned money or you’re tricked by an online scammer. What would you do? Most people don’t know where to start. Legal help feels expensive and complicated, leaving many without a fair chance to fight for their rights.**

  """)
if st.button('Try Nyaysathi now'):
 st.switch_page("nyaysathi.py") 
