import streamlit as st
import os

# MUST BE FIRST!
st.set_page_config(layout="wide")

#Hide sidebar completely
st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)

#Display trailer only if available
if "selected_trailer" in st.session_state and st.session_state["selected_trailer"]:
    trailer_path = st.session_state["selected_trailer"]

    # Title (optional)
    st.title("🎞 Now Streaming Trailer")

    # Check if trailer file exists
    if os.path.exists(trailer_path):
        # Center the video with 15%-70%-15% column layout
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.video(trailer_path)
    else:
        st.error(f"❌ Trailer file not found at path: {trailer_path}")
else:
    st.warning("⚠ No trailer selected. Please go back and select a movie.")

# Centered Back button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("🔙 Back to Movie Selection"):
        st.switch_page("pages/1_Movie_Selection.py")
