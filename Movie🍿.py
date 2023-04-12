import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np



def fetch_poster(mv_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=af351bb5330b7cdfef2359aa31207c94&language=en-US'.format(mv_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:20]

    recommended_movieposter=[]
    recommended_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch mv poster fromapi
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movieposter.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movieposter


similarity= pickle.load(open('recom.pkl', 'rb'))


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)

import base64
#Set page layout to wide
st.set_page_config(layout="wide")

# Load the background image
bg_image = open("mv1.jpg", "rb").read()

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








st.markdown("<h1 style='text-align: center; color: black;'>MOVIE RECOMMENDER</h1>", unsafe_allow_html=True)

# st.title('MOVIE RECOMMENDER')
selected_movie_name= st.selectbox(
    "How would to like to bo contacted?",
    sorted( movies['title'].values)
)
if st.button('Recommend'):
    names,posters= recommend(selected_movie_name)


    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])



    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.text(names[6])
        st.image(posters[6])
    with col2:
        st.text(names[7])
        st.image(posters[7])
    with col3:
        st.text(names[8])
        st.image(posters[8])
    with col4:
        st.text(names[9])
        st.image(posters[9])
    with col5:
        st.text(names[10])
        st.image(posters[10])
    with col6:
        st.text(names[11])
        st.image(posters[11])


    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.text(names[12])
        st.image(posters[12])
    with col2:
        st.text(names[13])
        st.image(posters[13])
    with col3:
        st.text(names[14])
        st.image(posters[14])
    with col4:
        st.text(names[15])
        st.image(posters[15])
    with col5:
        st.text(names[16])
        st.image(posters[16])
    with col6:
        st.text(names[17])
        st.image(posters[17])