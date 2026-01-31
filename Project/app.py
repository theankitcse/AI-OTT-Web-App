import streamlit as st
import pickle
import pandas as pd
import requests
import time

API_KEY = 'b51a868627c338ab16664c7b141a7ba9'

def fetch_poster(movie_id, retries=3, delay=2):
    for attempt in range(retries):
        try:
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"
        except requests.exceptions.RequestException as e:
            print(f"[fetch_poster] Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"

def fetch_movie_details(movie_id, retries=3, delay=2):
    details = {
        'overview': 'No description available.',
        'genres': 'N/A',
        'release_date': 'N/A',
        'rating': 'N/A',
        'cast_info': []
    }
    for attempt in range(retries):
        try:
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            cast_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US'
            cast_response = requests.get(cast_url, timeout=10)
            cast_response.raise_for_status()
            cast_data = cast_response.json()
            cast_members = cast_data.get('cast', [])[:5]

            cast_info = []
            for member in cast_members:
                name = member['name']
                profile_path = member.get('profile_path')
                image_url = f"https://image.tmdb.org/t/p/w500{profile_path}" if profile_path else "https://via.placeholder.com/150"
                cast_info.append({'name': name, 'image': image_url})

            details = {
                'overview': data.get('overview', details['overview']),
                'genres': ', '.join([genre['name'] for genre in data.get('genres', [])]) or details['genres'],
                'release_date': data.get('release_date', details['release_date']),
                'rating': data.get('vote_average', details['rating']),
                'cast_info': cast_info
            }
            return details
        except requests.exceptions.RequestException as e:
            print(f"[fetch_movie_details] Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)

    return details

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movie_ids = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movie_id)
        recommended_movies_poster.append(poster_url)
        recommended_movie_ids.append(movie_id)
        print(f"[recommend] Movie: {movies.iloc[i[0]].title}, TMDB ID: {movie_id}, Poster URL: {poster_url}")

    return recommended_movies, recommended_movies_poster, recommended_movie_ids

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('OTT AI BASED MOVIE WEB APP')

selected_movie_name = st.selectbox('Select a Movie You Like:', movies['title'].values)

if st.button('Recommend'):
    names, posters, movie_ids = recommend(selected_movie_name)
    st.session_state.names = names
    st.session_state.posters = posters
    st.session_state.movie_ids = movie_ids

if 'names' in st.session_state:
    names = st.session_state.names
    posters = st.session_state.posters
    movie_ids = st.session_state.movie_ids

    st.markdown("### Recommended Movies:")
    cols = st.columns(5)
    for idx in range(len(names)):
        with cols[idx % 5]:
            st.markdown(
                f"<div style='text-align:center; font-weight:bold; font-size:16px; height:50px; color:white'>{names[idx]}</div>",
                unsafe_allow_html=True
            )
            st.image(posters[idx], use_container_width=True)

    selected_info_movie = st.selectbox("Click to view movie details:", options=["Select a movie to view details"] + list(names))

    if selected_info_movie != "Select a movie to view details":
        selected_index = names.index(selected_info_movie)
        details = fetch_movie_details(movie_ids[selected_index])

        st.markdown("---")
        st.subheader(f"Details for: {selected_info_movie}")
        st.markdown(f"**Overview:** {details['overview']}")
        st.markdown(f"**Genres:** {details['genres']}")
        st.markdown(f"**Release Date:** {details['release_date']}")
        st.markdown(f"**Rating:** {details['rating']}")

        st.markdown("### Main Cast:")
        num_cast = min(len(details['cast_info']), 5)
        if num_cast > 0:
            cast_cols = st.columns(num_cast)
            for i, cast in enumerate(details['cast_info'][:5]):
                with cast_cols[i]:
                    st.image(cast['image'], caption=cast['name'], use_container_width=True)
        else:
            st.write("No cast information available.")
