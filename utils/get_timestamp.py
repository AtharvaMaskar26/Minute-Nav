import dotenv
from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

def get_timestamps(transcript, question):
    """
    description: 
        This function takes the question and transcript and guides the user to the exact timestamp of the video 
    parameters: 
        transcript (string): transcript of the video along with timestamps
        question (string): Question asked by the user
    returns:
        timestamp (string): Timestamp where the question occurs. 
    """
    prompt = f"You are a YouTube video helper, you will be given a transcript string with time stamps. Along with that you will be given a question. You have to return the timestamp where the topic is present. The transcripts with timestamps are: {transcript} and the question  is {question}. Return the exact timestamp"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e: 
        print(f"Error generating answer: {e}")


