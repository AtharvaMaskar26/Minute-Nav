import streamlit as st 
from streamlit_player import st_player

from sentence_transformers import SentenceTransformer

from utils import display_sidebar_links
from utils import generate_answer
from utils import get_video_id
from utils import is_link_valid
from utils import get_video_trascript
from utils import get_timestamp
from utils import process_timestamps


def embed_sentences(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

display_sidebar_links()

st.header("QnA")


with st.form("my-form"):
    video_link = st.text_input("Enter YouTube link: ")
    submitted = st.form_submit_button("Submit")

    if submitted: 
        if is_link_valid(video_link):
            video_id = get_video_id(video_link)
            transcript, transcript_text = get_video_trascript(video_id)
            sentences = [item['text'] for item in transcript]
            embeddings = embed_sentences(sentences)

            question = st.text_input("Ask your question")
            timestamp = get_timestamp(question, transcript, embeddings)

            answer = generate_answer(question, transcript_text)

            # st_player(video_link)

            if question:
                st.header("Ask any questions:")
                st.write(answer)

                if timestamp:
                    st.write(f"Topic was covered here: {timestamp}")
                    st_player(f"{video_link}={int(timestamp)}s")
                else:
                    st.write("Topic not found in the transcript.")
        else:
            st.warning("Enter valid YouTube link")