import streamlit as st
import shelve

# Load environment variables (assuming you have set them u

# Using generativeai for Google Cloud Generative AI
import google.generativeai as genai
# Create a Generative AI client (moved outside the loop)

st.title("Nyaysathi")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"
genai.configure(api_key="AIzaSyDNcp_JDchji_PfU6mKwjCz2SxGBj0a4Ow")
# Ensure model_name is initialized in session state
if "model_name" not in st.session_state:
    st.session_state["key"] = "models/flash8b"  # Update with your desired model

# Load chat history from shelve file
def load_chat_history():
    try:
        with shelve.open("chat_history") as db:
            return db.get("messages", [])
    except Exception as e:
        st.error(f"Error loading chat history: {e}")
        return []

# Save chat history to shelve file
def save_chat_history(messages):
    try:
        with shelve.open("chat_history") as db:
            db["messages"] = messages
    except Exception as e:
        st.error(f"Error saving chat history: {e}")

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])
        st.success("Chat history deleted.")

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("How can I help?"):
    # Add user input to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

prompti = (f"{prompt}(you are an indian legal specialist, who helps people with justice so answer this question like a legal assistant of India)")
    # Generate and display the assistant's response
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        try:
            with st.spinner("Generating response..."):
               model=genai.GenerativeModel("gemini-1.5-flash")
               response= model.generate_content(prompti)
               message_placeholder.markdown(response.text)
            print(response)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

        except Exception as e:
            message_placeholder.markdown("An error occurred while generating a response.")
            st.error(f"Error: {e}")

# Save chat history after each interaction
save_chat_history(st.session_state.messages)
