import streamlit as st

def display_sidebar_links():
    st.sidebar.page_link("pages/qna.py", label="QnA")
    st.sidebar.page_link("pages/summary.py", label="Video Summary")