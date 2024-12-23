import streamlit as st
from streamlit_extras.switch_page_button import switch_page
hide = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden}
header {visibility:hidden}
</style>
"""
st.markdown(hide, unsafe_allow_html = True)
# Icon for title
icon1 = ":material/description:"
# Content of the introduction
col1,col2 = st.columns(2, gap ="small", vertical_alignment ="center")
with col1:
  st.title(f"Introduction {icon1}")
with col2:
  st.image("Screenshot (2).png", width=230)
st.markdown("## **Nyaysathi**")
c1,c2 = st.columns(2, gap="medium", vertical_alignment="bottom")
with c1:
  st.image("DALL·E 2024-12-23 18.56.53 - A highly realistic and emotional illustration showing poor people living on the streets of India, with a backdrop of crowded streets and humble shelte.webp", width=230)
with c2:
  st.markdown("""NyaySathi: A perfect legal Assistant

  **Imagine you’re in a situation where someone refuses to return your hard-earned money or you’re tricked by an online scammer. What would you do? Most people don’t know where to start. Legal help feels expensive and complicated, leaving many without a fair chance to fight for their rights.**

  """)
st.write("""
NyaySathi was born from a simple yet powerful idea: justice should be accessible to everyone, regardless of their background or resources. This is where NyaySathi steps in—a smart AI platform built to ensure justice for everyone, no matter their background or income. NyaySathi simplifies legal processes, helps you understand your rights, and guides you step-by-step, whether it's reporting cybercrimes or resolving disputes.

""")  
colu1,colu2= st.columns(2, gap="medium", vertical_alignment="top")
with colu1:
  st.write("""
  For instance, if someone accidentally breaks a rule they didn’t understand, NyaySathi doesn’t just lecture them. It provides the right advice on how to make amends and stay lawful in the future.
  I created NyaySathi because I believe justice should be accessible to all. In India, many people miss out on fair outcomes because they can’t afford lawyers or don’t know where to start.
  With NyaySathi, you’ll have the tools to stand up for your rights confidently and contribute to a safer, more peaceful society.
  """)
with colu2:
  st.image("DALL·E 2024-12-23 18.57.05 - A vibrant and uplifting illustration showcasing the essence of NyaySathi_ a diverse group of people interacting with an AI-powered justice platform in.webp",width=230)
st.write("""
 Let’s create a world where everyone feels protected—try NyaySathi today and be part of the change.

""")
if st.button('Nyaysathi'):
 st.switch_page("nyaysathi.py") 
