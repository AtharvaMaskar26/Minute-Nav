import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

prompt = "You are a YouTube video summarizer. You will be taking the transcript text and have to give the summary in return. People coming to you are looking for something that would give them the idea of the video at one place without having to go through the entire video. Generate a detailed summary of this educational video that provides a thorough overview of the topic discussed. Include key points, main ideas, supporting arguments, and any relevant examples or explanations provided in the video.The summary should be structured and coherent, presenting the information in a logical sequence to aid understanding. Aim to capture the essence of the video in a concise and informative manner, suitable for someone seeking to gain a comprehensive understanding of the topic without watching the entire video "

def generate_summary(transcript_text):
    """
    Description:
        This function takes the transcript and returns summary using the google gemini model. 

    Parameters: 
        transcript (str): Transcripts of the youtube video you want to get summary of

    returns: 
        summary (str): Summary of the transcript
    """
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        respone = model.generate_content(prompt + transcript_text)
    except Exception as e: 
        print(f"Error generating summary: {e}")

    return respone.text