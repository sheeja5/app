import streamlit as st

# Function to display the navigation bar
def navigation_bar():
    # Horizontal navigation using a selectbox or radio buttons
    menu = ['About', 'Nyaysathi']
    choice = st.selectbox("Select Page", menu)
    return choice

# Main function to navigate based on selection
def main():
    # Display the navigation bar
    choice = navigation_bar()

    # Redirect to the appropriate page
    if choice == 'About':
        st.write("Redirecting to About Page...")
        st.experimental_set_query_params(page="about")  # Optional, useful for URL routing in Streamlit
        st.markdown('<a href="about.py" target="_self">Go to About</a>', unsafe_allow_html=True)
    elif choice == 'Nyaysathi':
        st.write("Redirecting to Nyaysathi Page...")
        st.experimental_set_query_params(page="nyaysathi")  # Optional
        st.markdown('<a href="nyaysathi.py" target="_self">Go to Nyaysathi</a>', unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()

