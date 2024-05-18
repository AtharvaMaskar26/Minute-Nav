import dotenv
from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

def generate_answer(question, transcript_text):
    """
    Description:
        This function is a part of the QnA system, that allows you to ask questions to any YouTube video provided. This function takes the question and returns the answer from the context of the transcript. 

    parameters: 
        question (str): Question asked by the user
        transcript_text (str): transcript of the YouTube Video
        
    returns: 
        answer (str): Answer 
    """
    questions_asked = "Previously asked questions are as follows: \n"
    counter = 0

    prompt = f"You are a YouTube video helper bot. You will be given a transcript and the user will ask you questions related to the transcript. You will also have a list of questions and responses by you that have been asked by the user so far and your answers to it, so if the user asks a followup questions try to answer that.You only have to answer questions that are in the transcript and only in context of the Youtube video (Transcript) provided. Transcript text is as follows: {transcript_text} and the question asked by the user is: {question}."

    try:
        model = genai.GenerativeModel("gemini-pro")
        final_prompt = prompt + questions_asked
        response = model.generate_content(final_prompt)
        counter += 1
        questions_asked += f"{counter}. Question: {question} \n response: {response}"
        return response.text
    except Exception as e: 
        print(f"Error generating answer: {e}")
