
import streamlit as st

# Define function for home page
def home_page():
    page_bg_img = '''
    <style>
    body {
        background-image: url("wallpaper.jpeg");
        background-size: cover;
    }
    </style>
    '''

# Display the custom CSS
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Display the PNG image with center alignment and smaller width
    st.button("About Us")
    st.image("dream.jpeg", use_column_width=True)
    st.title(" Welcome to [Team Name] ")
    st.write("""
In today’s fast-paced world, a good night’s sleep is more than a luxury; it’s a cornerstone of health and happiness. [Team Name] is designed to be your companion in the quest for restful nights and energized mornings.

Our app doesn’t just track your sleep; it transforms it. By harnessing the power of advanced analytics and personalized insights, SlumberSage offers a comprehensive overview of your sleep patterns. Understand the phases of your slumber, identify disturbances, and receive tailored advice to enhance the quality of your rest.
if you need help with the description on the home page
    """)

    # Button 2 in the second column
    st.markdown("<div class='center'>", unsafe_allow_html=True)
    if st.button("Stress Prediction"):
        Stress_predict_page()
    st.markdown("</div>", unsafe_allow_html=True)



def Stress_predict_page():
    st.title("Welcome to the stress level predictor")
    st.write("Enter your information to see which level of stress you may be (0-4, 0 being the lowest")
    
    

# Use a selectbox for page navigatio
page = st.sidebar.selectbox("Choose a page", ["Home", "Data Visualization"])

#Render the selected page:
if page == "Home":
    home_page()
elif page == "Data Visualization":
    home_page()
