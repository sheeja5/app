import streamlit as st

# Setting a background image
def set_background(image_path):
    """
    Sets a background image for the Streamlit app.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_path});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Path to the background image
background_image = "Screenshot (1).png"  # Replace with the actual path to the image
set_background(background_image)

# Icon for title
icon1 = ":material/description:"

# Content of the introduction
st.title(f"Introduction {icon1}")
st.markdown("## **Nyaysathi**")
st.write("""
A perfect AI for legal assistance

This AI aims to make use of its knowledge to ensure that all the people of India are feeling safe. A peaceful surrounding is created with “ZERO” number of conflict among the people of India. This AI platform can also be situational-based, like if a person commits some kind of crime by mistake, this AI could help that person by leading him/her to a rightful way to deal with it.

I created NyaySathi because I believe that everyone deserves access to justice, regardless of their income or background. In India, many people are unable to afford legal representation, which can lead to unfair outcomes in court.

NyaySathi is designed to help people understand their legal rights and options, and to navigate the complex legal system. I hope that NyaySathi will empower people to fight for their rights and achieve justice. It can also lessen the number of Cyber Crimes that are increasing daily.
""")
