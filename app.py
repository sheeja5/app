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
        st.markdown('<a href="about_me.py" target="_self">Go to About</a>', unsafe_allow_html=True)
    elif choice == 'Nyaysathi':
        st.write("Redirecting to Nyaysathi Page...")
        st.markdown('<a href="Nyaysathi.py" target="_self">Go to Nyaysathi</a>', unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()

