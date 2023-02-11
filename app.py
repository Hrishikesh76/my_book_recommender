import streamlit as st
import pickle
import numpy as np

similarity_score = pickle.load(open('similarity_score.pkl','rb'))
pt = pickle.load(open('movies.pkl','rb'))


def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    for i in similar_items:
        st.write(pt.index[i[0]])


book_list = pickle.load(open('movies.pkl','rb'))
book_list = book_list.index

st.title('My Book Recommender System')

selected_book_name = st.selectbox(
    'Type the name of book or choose from dropdown to recommend?',
    book_list)

if st.button('Recommend'):
    books = recommend(selected_book_name)
