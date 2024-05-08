from youtube_transcript_api import YouTubeTranscriptApi

def get_video_trascript(video_id):
    """
    description: 
        Takes the video id, uses the youtube video transcript api to generate transcripts

    parameters: 
        video_id (str): Id of the YouTube video 

    returns: 
        transcript_array (array): Transcript of the YouTube Video along with duration and start time
        transcript_text (str): Text transcript of the video. 
    """

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ''
        for line in transcript:
            transcript_text += line['text'] + ' '
    except Exception as e:
        print("Error while getting transcript:", e)

    
    return transcript, transcript_text


    