import streamlit as st
from results_page import display_results_page  # Ensure this import works based on your directory structure

# Set page layout to wide mode for better control of the columns
st.set_page_config(layout="wide")

# Display the app title
st.markdown("<h1 style='text-align: center; color: black; margin-bottom: 2rem;'>Factify</h1>", unsafe_allow_html=True)

# Create columns for the search bar and button with a specific ratio
col1, col2 = st.columns([0.8, 0.2], gap="small")

with col1:
    user_query = st.text_input("", placeholder="Enter your query here...", key="search_input")

with col2:
    search_button = st.button("Search", key="search_button")

if search_button and user_query:  # Check if the search button is pressed and there is a query
    st.session_state.user_query = user_query  # Store the user query in session state
    st.session_state.page = 'results'  # Set the session state to navigate to results

# Navigation logic based on session state
if 'page' in st.session_state and st.session_state.page == 'results':
    display_results_page()
else:
    # This is where you could put any additional code for the main page if needed
    pass

# Optional: Custom CSS for styling
st.markdown("""
<style>
/* Custom styles */
</style>
""", unsafe_allow_html=True)
