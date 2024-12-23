import streamlit as st
# Icon for title
icon1 = ":material/description:"
# Content of the introduction
col1,col2 = st.columns(2, gap ="small", vertical_alignment ="center")
with col1:
  st.title(f"Introduction {icon1}")
with col2:
  st.image("Screenshot (2).png", width=230)
st.markdown("## **Nyaysathi**")
st.write("""
A perfect AI for legal assistance

This AI aims to make use of its knowledge to ensure that all the people of India are feeling safe. A peaceful surrounding is created with “ZERO” number of conflict among the people of India. This AI platform can also be situational-based, like if a person commits some kind of crime by mistake, this AI could help that person by leading him/her to a rightful way to deal with it.

I created NyaySathi because I believe that everyone deserves access to justice, regardless of their income or background. In India, many people are unable to afford legal representation, which can lead to unfair outcomes in court.

NyaySathi is designed to help people understand their legal rights and options, and to navigate the complex legal system. I hope that NyaySathi will empower people to fight for their rights and achieve justice. It can also lessen the number of Cyber Crimes that are increasing daily.
""")
st.link_button('Try Nyaysathi now','https://2xbjtqbfkb2zwbev7prccj.streamlit.app/Nyaysathi')
