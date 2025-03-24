import streamlit as st
import google.generativeai as genai
# Initialize Google Cloud Language client
# Function to generate a complaint letter using Google Generative AI
genai.configure(api_key="AIzaSyDNcp_JDchji_PfU6mKwjCz2SxGBj0a4Ow")
def generate_complaint_letter(details):
    prompt = f"""Write a formal police complaint letter based on the following details and use this format to write[Your Name]
               [Your Address]
               [City, State, PIN Code]
               [Email Address]
               [Phone Number]

                [Date]

               The Station House Officer
               [Name of Police Station]
               [Station Address]
               [City, State, PIN Code]

               Subject: Complaint Regarding [brief description of the incident]

               Respected Sir/Madam,

                I, [Your Name], residing at [Your Address], wish to bring to your attention an incident that occurred on [Date] at approximately [Time] at [Location]. [Provide a detailed description of the incident, including any individuals involved and witnesses, if applicable.]

               This incident has caused me significant distress, and I request that you register my complaint and initiate an investigation into the matter. I am willing to provide any further information or assistance required.

               Thank you for your attention to this matter.

               Yours sincerely,

               [Your Signature]

               [Your Name]


               :\n{details}"""
    
    # Assuming Google Generative AI client has a similar interface
    
     
   
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    generated_text = model.generate_content(prompt)

    # Here, you'd use the appropriate API call for text generation.
    # The line below is a placeholder for the actual generative AI function.
   # Modify as per actual API response structure
    
    return generated_text.text

# Streamlit UI
st.title("**NYAYSATHI**: Complaint Letter Generator")

st.subheader("Enter the details of your complaint:")
details = st.text_area("Describe the incident here (include what happened, when, where, and who was involved):")

if st.button("Generate Complaint Letter"):
    if details:
        with st.spinner('Generating your complaint letter...'):
          letter = generate_complaint_letter(details)
          st.subheader("Generated Complaint Letter:")
          st.text_area("Complaint Letter", value=letter, height=300)
          st.warning("Please review and edit the generated complaint letter carefully before using it. Ensure all details are accurate and complete.This can make mistakes")
          st.download_button(
                label="Download Complaint Letter",
                data=letter,
                file_name = "complaint_letter.txt",
                mime="text/plain"
          )    
    else:
        st.warning("Please enter the details of your complaint.")
