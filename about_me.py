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
st.markdown("""NyaySathi: A perfect legal Assistant

**Imagine you’re in a situation where someone refuses to return your hard-earned money or you’re tricked by an online scammer. What would you do? Most people don’t know where to start. Legal help feels expensive and complicated, leaving many without a fair chance to fight for their rights.**

NyaySathi was born from a simple yet powerful idea: justice should be accessible to everyone, regardless of their background or resources. This is where NyaySathi steps in—a smart AI platform built to ensure justice for everyone, no matter their background or income. NyaySathi simplifies legal processes, helps you understand your rights, and guides you step-by-step, whether it's reporting cybercrimes or resolving disputes.

For instance, if someone accidentally breaks a rule they didn’t understand, NyaySathi doesn’t just lecture them. It provides the right advice on how to make amends and stay lawful in the future.

I created NyaySathi because I believe justice should be accessible to all. In India, many people miss out on fair outcomes because they can’t afford lawyers or don’t know where to start. With NyaySathi, you’ll have the tools to stand up for your rights confidently and contribute to a safer, more peaceful society.

Let’s create a world where everyone feels protected—try NyaySathi today and be part of the change.
""")
st.link_button('Try Nyaysathi now','https://2xbjtqbfkb2zwbev7prccj.streamlit.app/Nyaysathi')
