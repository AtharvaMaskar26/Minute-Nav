import streamlit as st

def process_transcript(transcripts):
    """
    description:
        This function takes the transcript aray and returns a more meaningful transcript better for generating response

    parameters: 
        transcripts (array): Array containing transcript texts, start time and duration

    returns: 
        processed_transcript (str): Processes more meaningful transcript
    """

    processed_transcript = ""
    for transcript in transcripts: 
        start = transcript['start']
        duration = transcript['duration']
        end = start + duration

        start /= 60
        start = format(start, ".2f")
        end /= 60
        end = format(end, ".2f")
        processed_transcript += f"{start} - {end} : {transcript['text']}\n\n"

    return processed_transcript