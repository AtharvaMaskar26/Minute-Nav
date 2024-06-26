import streamlit as st
from streamlit_player import st_player


from utils import display_sidebar_links
from utils import generate_summary
from utils import get_video_id
from utils import is_link_valid
from utils import get_video_trascript


# Displaying sidebar links
display_sidebar_links()


# Form
with st.form("my-form"):
    video_link = st.text_input("Enter YouTube link: ")
    submitted = st.form_submit_button("Get Summary")

    # Get video if for the link 
    if submitted: 
        if is_link_valid(video_link): 
            video_id = get_video_id(video_link)
            _, transcript_text = get_video_trascript(video_id)
            summary = generate_summary(transcript_text)
            st_player(video_link)
            st.header("Summary: ")
            st.write(summary)

        else:
            st.warning("Enter valid YouTube Link")
    

