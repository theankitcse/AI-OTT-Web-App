import streamlit as st  # For building interactive web apps
import os  # For file operations

#Configure Page Layout
st.set_page_config(layout="wide")  # Enables a wide layout for the app

#Hide Sidebar Completely
st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}  /* Hide sidebar */
    [data-testid="collapsedControl"] {display: none;}  /* Hide collapse button */
    </style>
""", unsafe_allow_html=True)  # Allows custom HTML and CSS for styling

#Check if Trailer is Selected
if "selected_trailer" in st.session_state and st.session_state["selected_trailer"]:
    trailer_path = st.session_state["selected_trailer"]  # Get the selected trailer path

    #Display Title
    st.title(" Now Streaming Trailer")

    #Check if Trailer File Exists
    if os.path.exists(trailer_path):
        #Display Video Centered
        col1, col2, col3 = st.columns([1, 3, 1])  # 15%-70%-15% column layout for centering
        with col2:
            st.video(trailer_path)  # Play the video
    else:
        st.error(f"Trailer file not found at path: {trailer_path}")  # Error if file is missing

else:
    st.warning("No trailer selected. Please go back and select a movie.")  # Warning if no trailer is selected

#Back to Movie Selection
st.markdown("<br>", unsafe_allow_html=True)  # Add spacing

#Centered Back Button
col1, col2, col3 = st.columns([2, 1, 2])  # 40%-20%-40% layout for centering
with col2:
    if st.button("🔙 Back to Movie Selection"):  # On button click
        st.switch_page("pages/1_Movie_Selection.py")  # Redirect to movie selection page
