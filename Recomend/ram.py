import streamlit as st
import pickle
import pandas as pd
import requests

#Helper Functions
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_movie_details(movie_id):
    #Movie Info
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    response = requests.get(url)
    data = response.json()

    #Cast Info
    cast_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    cast_response = requests.get(cast_url)
    cast_data = cast_response.json()
    cast_members = cast_data.get('cast', [])[:5]  # Top 5 cast

    cast_info = []
    for member in cast_members:
        name = member['name']
        profile_path = member.get('profile_path')
        image_url = f"https://image.tmdb.org/t/p/w500{profile_path}" if profile_path else "https://via.placeholder.com/150"
        cast_info.append({'name': name, 'image': image_url})

    #Details Dictionary
    details = {
        'overview': data.get('overview', 'No description available.'),
        'genres': ', '.join([genre['name'] for genre in data.get('genres', [])]),
        'release_date': data.get('release_date', 'N/A'),
        'rating': data.get('vote_average', 'N/A'),
        'cast_info': cast_info
    }
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
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movie_ids.append(movie_id)

    return recommended_movies, recommended_movies_poster, recommended_movie_ids

#Load Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

#App Title
st.title('🎬 OTT AI BASED MOVIE WEB APP')

#Background Video
st.markdown(
    """
    <style>
    .video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100vw;
        min-height: 100vh;
        z-index: -1;
        object-fit: cover;
    }
    .stApp {
        background: transparent;
    }
    </style>

    <video autoplay muted loop class="video-background">
        <source src="https://www.dropbox.com/scl/fi/kdq60m5larclkbueds68x/VID_20250319104941.mp4?rlkey=yv6h7hj4n2f2q4r286u1qywi2&st=pbrqbd0q&raw=1" type="video/mp4">
    </video>
    """,
    unsafe_allow_html=True
)

#Movie Selector
selected_movie_name = st.selectbox(
    '🎥 Select a Movie You Like:',
    movies['title'].values
)

#Recommendation Trigger or Button
if st.button('🚀 Recommend'):
    names, posters, movie_ids = recommend(selected_movie_name)
    st.session_state.names = names
    st.session_state.posters = posters
    st.session_state.movie_ids = movie_ids

#Show Recommendations if Present
if 'names' in st.session_state:
    names = st.session_state.names
    posters = st.session_state.posters
    movie_ids = st.session_state.movie_ids

    st.markdown("### 🎯 Recommended Movies:")
    cols = st.columns(5)
    for idx in range(len(names)):
        with cols[idx % 5]:
            st.markdown(
                f"<div style='text-align:center; font-weight:bold; font-size:16px; height:50px; color:white'>{names[idx]}</div>",
                unsafe_allow_html=True
            )
            st.image(posters[idx], use_container_width=True)

    # Movie detail selector
    selected_info_movie = st.selectbox("📖 Click to view movie details:", options=["Select a movie to view details"] + list(names))

    if selected_info_movie != "Select a movie to view details":
        selected_index = names.index(selected_info_movie)
        details = fetch_movie_details(movie_ids[selected_index])

        st.markdown("---")
        st.subheader(f"📘 Details for: {selected_info_movie}")
        st.markdown(f"**🎞 Overview:** {details['overview']}")
        st.markdown(f"**🎭 Genres:** {details['genres']}")
        st.markdown(f"**📅 Release Date:** {details['release_date']}")
        st.markdown(f"**⭐ Rating:** {details['rating']}")

        st.markdown("### 👥 Main Cast:")
        cast_cols = st.columns(len(details['cast_info']))
        for i, cast in enumerate(details['cast_info']):
            with cast_cols[i]:
                st.image(cast['image'], caption=cast['name'], use_container_width=True)
