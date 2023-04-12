import streamlit as st
import base64
# Set page title and favicon
st.set_page_config(page_title='College Project', page_icon=':mortar_board:',layout="wide")



# Load the background image
bg_image = open("tm.jpg", "rb").read()

# Add some CSS to style the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/jpeg;base64,{base64.b64encode(bg_image).decode()});
        background-size: cover;
        background-position: center center;
    }}
    </style>Home.run
    
    """,
    unsafe_allow_html=True,)

# Add header
st.title('College Project')

# Add description
st.write('Welcome to our college project! Here you can find information about our project and our team.')

# Add team section
st.header('Meet our team')

# Add team member information
col1, col2, col3 = st.columns(3)
with col1:
    st.image('tm.jpg', caption='John Doe')
with col2:
    st.image('tm.jpg', caption='Jane Doe')
with col3:
    st.image('tm.jpg', caption='Syed Mohd ALtamash')

# Add project section
st.header('Our project')

# Add project information
st.subheader('Project description')
st.write('Our project is about recommendation system ')

st.subheader('Project goals')
st.write('Our project aims to .....')

# Add footer
st.write('Thank you for visiting our college project website!')
