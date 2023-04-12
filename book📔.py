import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np
import base64
model=pickle.load(open('model.pkl', 'rb'))
books_name=pickle.load(open('books_name.pkl', 'rb'))
final_rating=pickle.load(open('final_rating.pkl', 'rb'))
book_pivot=pickle.load(open('book_pivot.pkl', 'rb'))



#Set page layout to wide
st.set_page_config(layout="wide")

# Load the background image
bg_image = open("new.jpg", "rb").read()

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







#st.title("RECOMMENDATION SYSTEM")
st.markdown("<h1 style='text-align: center; color:black;'>BOOK RECOMMENDER</h1>", unsafe_allow_html=True)


# st.title("BOOK RECOMMENDER")
selected_books=st.selectbox("type or select",
                            books_name)


def fetch_poster1(suggestion):
    book_name=[]
    ids_index=[]
    poster_url=[]


    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img-url']
        poster_url.append(url)

    return poster_url

    # except Exception as e:
    # raise AppException(e, sys) from e



def recommend_books(book_name):
    book_list=[]
    book_id=np.where(book_pivot.index==book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=17)

    poster_url=fetch_poster1(suggestion)

    for i in range(len(suggestion)):
        books=book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list,poster_url

if st.button('Recommend_book'):
    recommendation_books,poster_url=recommend_books(selected_books)



    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])


    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(recommendation_books[6])
        st.image(poster_url[6])
    with col2:
        st.text(recommendation_books[7])
        st.image(poster_url[7])
    with col3:
        st.text(recommendation_books[8])
        st.image(poster_url[8])
    with col4:
        st.text(recommendation_books[9])
        st.image(poster_url[9])
    with col5:
        st.text(recommendation_books[10])
        st.image(poster_url[10])


    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(recommendation_books[11])
        st.image(poster_url[11])
    with col2:
        st.text(recommendation_books[12])
        st.image(poster_url[12])
    with col3:
        st.text(recommendation_books[13])
        st.image(poster_url[13])
    with col4:
        st.text(recommendation_books[14])
        st.image(poster_url[14])
    with col5:
        st.text(recommendation_books[15])
        st.image(poster_url[15])

# st.title("book")