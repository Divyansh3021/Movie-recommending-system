import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6676272cd0ea0e6f7faf496de7c3ab06".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values
# st.title(len(movies_list))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key = lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_poster = []
    for i in  movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    '',
    movies_list
)

if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    # with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])

    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])
    with col6:
        st.text(name[5])
        st.image(posters[5])
    # with col7:
    #     st.header(name[6])
    #     st.image(posters[6])
    # with col8:
    #     st.header(name[7])
    #     st.image(posters[7])
    # with col9:
    #     st.header(name[8])
    #     st.image(posters[8])
    # with col10:
    #     st.header(name[9])
    #     st.image(posters[9])