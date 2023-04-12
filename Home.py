import streamlit as st
import base64
from streamlit_lottie import st_lottie
import json

#Set page layout to wide
st.set_page_config(layout="wide")

# Load the background image
bg_image = open("book3.jpg", "rb").read()

# Add some CSS to style the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/jpeg;base64,{base64.b64encode(bg_image).decode()});
        background-size: cover;
        
        background-position: center center;
    }}
    </style>
    """,
    unsafe_allow_html=True,)

st.markdown("<h1 style='text-align: center; color: green;'>RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)


header_html = "<h1 style='font-size: 36px; color: red;'></h1>"
st.write(header_html, unsafe_allow_html=True)

lottie_file = open('helloboy.json', 'r')
lottie_json = json.load(lottie_file)
st_lottie(lottie_json)


