import re

def is_link_valid(youtube_video_link):
    """
    Checks if the given link is a valid YouTube video link.

    parameters:
    - youtube_video_link (str): The link to check.

    Returns:
    - isValid (bool): true if the link is a valid YouTube link else false 
    """

    # Regular expression pattern for matching YouTube video URLs
    pattern = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"

    
    return re.match(pattern, youtube_video_link) is not None