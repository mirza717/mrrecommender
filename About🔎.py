import streamlit as st
import base64


#Set page layout to wide
st.set_page_config(layout="wide")

# Load the background image
bg_image = open("aboutt.jpg", "rb").read()

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


header_html = "<h1 style='font-size: 36px; color: black;'>What is Recommendation System?</h1>"
st.write(header_html, unsafe_allow_html=True)


# Define the paragraph text with HTML tags for formatting
text = "<p style='font-size:24px;color:black;'>Recommender systems are the systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the users are most likely to purchase and are of interest to. Companies like Netflix, Amazon, etc. use recommender systems to help their users to identify the correct product or movies for them.</p>"
# Display the paragraph using the st.markdown() function
st.markdown(text, unsafe_allow_html=True)

text1 = "<p style='font-size:24px;color:black;'>The recommender system deals with a large volume of information present by filtering the most important information based on the data provided by a user and other factors that take care of the user’s preference and interest. It finds out the match between user and item and imputes the similarities between users and items for recommendation. </p>"
# Display the paragraph using the st.markdown() function
st.markdown(text1, unsafe_allow_html=True)

header_html = "<h1 style='font-size: 36px; color: black;'>Movie Recommendation System</h1>"
st.write(header_html, unsafe_allow_html=True)

text2 = "<p style='font-size:24px;color:black;'>Content Based Recommendation System: It uses attributes such as genre, director, description, actors, etc. for movies, to make suggestions for the users. The intuition behind this sort of recommendation system is that if a user liked a particular movie or show, he/she might like a movie or a show similar to it. </p>"
# Display the paragraph using the st.markdown() function
st.markdown(text2, unsafe_allow_html=True)

header_html = "<h1 style='font-size: 36px; color: black;'>Book Recommendation System</h1>"
st.write(header_html, unsafe_allow_html=True)

text3 = "<p style='font-size:24px;color:black;'>Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users.</p>"
# Display the paragraph using the st.markdown() function
st.markdown(text3, unsafe_allow_html=True)

text4 = "<p style='font-size:24px;color:black;'>It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. It looks at the items they like and combines them to create a ranked list of suggestions.</p>"
# Display the paragraph using the st.markdown() function
st.markdown(text4, unsafe_allow_html=True)

text5 = "<p style='font-size:24px;color:black;'>There are many ways to decide which users are similar and combine their choices to create a list of recommendations.</p>"

# Display the paragraph using the st.markdown() function
st.markdown(text5, unsafe_allow_html=True)
text8 = "<p style='font-size:24px;color:black;'>To address some of the limitations of content-based filtering, collaborative filtering uses similarities between users and items simultaneously to provide recommendations. This allows for serendipitous recommendations; that is, collaborative filtering models can recommend an item to user A based on the interests of a similar user B. Furthermore, the embeddings can be learned automatically, without relying on hand-engineering of features.</p>"

# Display the paragraph using the st.markdown() function
st.markdown(text8, unsafe_allow_html=True)

header_html = "<h1 style='font-size: 36px; color: black;'>Datasets</h1>"
st.write(header_html, unsafe_allow_html=True)


text6 = "<p style='font-size:24px;color:black;'>FOR MOVIES:</p>"
# Display the paragraph using the st.markdown() function
st.markdown(text6, unsafe_allow_html=True)

st.write("Click [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv) to go to movies dataset.")
text6 = "<p style='font-size:24px;color:black;'>FOR BOOKS:</p>"
# Display the paragraph using the st.markdown() function
st.markdown(text6, unsafe_allow_html=True)

st.write("Click [here](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) to go to book dataset.")
