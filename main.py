from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

def extract_video_id(url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)'
    match = re.match(pattern, url)
    return match.group(1) if match else None

def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

def embed_sentences(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

def find_relevant_timestamp(question, transcript, embeddings):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, embeddings)
    most_similar_idx = np.argmax(similarities)
    return transcript[most_similar_idx]['start']

def main(video_url, question):
    video_id = extract_video_id(video_url)
    transcript = get_transcript(video_id)
    sentences = [item['text'] for item in transcript]
    embeddings = embed_sentences(sentences)
    timestamp = find_relevant_timestamp(question, transcript, embeddings)
    if timestamp:
        print(f"The topic was covered at timestamp: {timestamp} seconds")
    else:
        print("Topic not found in the transcript.")

video_url = "https://youtu.be/2PeYDphtHYo?si=qT8C8nTNtgJ_YO0M"
question = "Who is Netanyahu?"
main(video_url, question)
