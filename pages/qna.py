import streamlit as st 
from streamlit_player import st_player

from utils import display_sidebar_links
from utils import generate_answer
from utils import get_video_id
from utils import is_link_valid
from utils import get_video_trascript
from utils import process_transcript
from utils import get_timestamps

display_sidebar_links()

st.header("QnA")


with st.form("my-form"):
    video_link = st.text_input("Enter YouTube link: ")
    submitted = st.form_submit_button("Submit")

    if submitted: 
        if is_link_valid(video_link):
            video_id = get_video_id(video_link)
            transcript, transcript_text = get_video_trascript(video_id)

            st_player(video_link)

            st.header("Ask any questions:")


            question = st.text_input("Ask your question")

            answer = generate_answer(question, transcript_text)

            st.write(answer)

            processesed_transcript = process_transcript(transcript)
            timestamps = get_timestamps(processesed_transcript, question)

            st.write(timestamps)



    else:
        st.warning("Enter valid YouTube link")