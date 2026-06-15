import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if not poster_path:
            return ""

        return "https://image.tmdb.org/t/p/w500/" + poster_path

    except Exception as e:
        print("TMDB Error:", e)
        return ""

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    # col1, col2, col3, col4, col5 = st.columns(5)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])

            if recommended_movie_posters[i]:
                st.image(recommended_movie_posters[i])
            else:
                st.write("Poster not available")



