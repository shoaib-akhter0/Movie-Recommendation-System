import streamlit as st
import pickle

from poster import fetch_poster

# Load Data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


# Recommendation Function
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# ---------------- Streamlit UI ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    movie_names, movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(movie_posters[0])
        st.caption(movie_names[0])

    with col2:
        st.image(movie_posters[1])
        st.caption(movie_names[1])

    with col3:
        st.image(movie_posters[2])
        st.caption(movie_names[2])

    with col4:
        st.image(movie_posters[3])
        st.caption(movie_names[3])

    with col5:
        st.image(movie_posters[4])
        st.caption(movie_names[4])