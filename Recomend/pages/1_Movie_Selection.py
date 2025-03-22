import streamlit as st

st.set_page_config(layout="wide")

# Movie List
movies_info = [
    {
        "title": "Krish3",
        "poster": "https://m.media-amazon.com/images/M/MV5BMjI0MzU3MTM1Ml5BMl5BanBnXkFtZTgwOTk2MjQ0MDE@._V1_.jpg",
        "trailer": "trailers/krish3.mp4"
    },
    {
        "title": "Interstellar",
        "poster": "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
        "trailer": "trailers/interstellar.mp4"
    },
    {
        "title": "The Dark Knight",
        "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "trailer": "trailers/The_Dark_Knight.mp4"
    },
    {
        "title": "Avengers: Endgame",
        "poster": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "trailer": "trailers/Avengers_Endgame.mp4"
    },
    {
        "title": "Spider-Man",
        "poster": "https://i.pinimg.com/originals/80/75/54/807554696e5f7893a335e54d922d83dc.jpg",
        "trailer": "trailers/Spider-man.mp4"
    }
]

# Style for Poster & Button
poster_width = "200px"
poster_height = "300px"

# UI Title
st.title("🎬 Featured Movies ")

# 🔍 Search Bar
search_query = st.text_input("Search for a movie...", "").strip().lower()

# Filter Movies based on Search
if search_query:
    filtered_movies = [movie for movie in movies_info if search_query in movie['title'].lower()]
else:
    filtered_movies = movies_info

if not filtered_movies:
    st.warning("No movies found for your search. Please try something else.")
else:
    cols = st.columns(5)

    for idx, movie in enumerate(filtered_movies):
        col = cols[idx % 5]
        with col:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{movie['poster']}" 
                         style="width:{poster_width}; height:{poster_height}; object-fit: cover; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                    <p style="margin-top: 10px; font-weight: bold;">{movie['title']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("▶ Watch Now", key=movie["title"]):
                st.session_state["selected_trailer"] = movie["trailer"]
                st.switch_page("pages/2_Trailer_Streaming.py")
