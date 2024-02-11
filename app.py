import streamlit as st

# Define a function for each page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def data_visualization_page():
    st.title("Data Visualization")
    st.write("Here are some data visualizations.")

# Use a selectbox for page navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Data Visualization"])

# Render the selected page
if page == "Home":
    home_page()
elif page == "Data Visualization":
    data_visualization_page()
