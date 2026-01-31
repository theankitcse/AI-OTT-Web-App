import streamlit as st  # For building the interactive web app UI

# Configure page layout to wide
st.set_page_config(layout="wide")

# List of Movies with Poster and Trailer Paths
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
        "trailer": "trailers/Spider-man_1.mp4"
    }
]

#Poster Styling
poster_width = "200px"
poster_height = "300px"

#App Title
st.title(" Featured Movies")

#Search Bar for Filtering Movies
search_query = st.text_input("Search for a movie...", "").strip().lower()  # Takes input and converts to lowercase

#Filter Movies Based on Search Query
if search_query:
    filtered_movies = [movie for movie in movies_info if search_query in movie['title'].lower()]
else:
    filtered_movies = movies_info  # Show all movies if search is empty

#If No Movies Match the Search
if not filtered_movies:
    st.warning("No movies found for your search. Please try something else.")

else:
    #Create Responsive Columns (Max 5 per row)
    cols = st.columns(5)

    for idx, movie in enumerate(filtered_movies):
        col = cols[idx % 5]  # Assign movie to a column in a row
        with col:
            #Display Poster with Styling
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{movie['poster']}" 
                         style="width:{poster_width}; height:{poster_height}; object-fit: cover; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                    <p style="margin-top: 10px; font-weight: bold;">{movie['title']}</p>
                </div>
                """,
                unsafe_allow_html=True  # Enables HTML for styling
            )

            #Button to Watch Trailer
            if st.button("▶ Watch Now", key=movie["title"]):
                st.session_state["selected_trailer"] = movie["trailer"]  # Store trailer path in session state
                st.switch_page("pages/2_Trailer_Streaming.py")  # Redirect to trailer streaming page
