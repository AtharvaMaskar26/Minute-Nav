import dotenv
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

def get_timestamp(question, transcript, embeddings):
    """
    description: 
        This function takes the question, transcript and embeddings and guides the user to the exact timestamp of the video 
    parameters: 
        transcript (string): transcript of the video along with timestamps
        question (string): Question asked by the user
        embeddwings: Numerical representation
    returns:
        timestamp (string): Timestamp where the question occurs. 
    """

    model = SentenceTransformer('all-MiniLM-L6-v2')
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, embeddings)
    most_similar_idx = np.argmax(similarities)


    return transcript[most_similar_idx]['start']


