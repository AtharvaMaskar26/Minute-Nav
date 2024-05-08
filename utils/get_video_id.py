def get_video_id(video_link):
    """
    description: 
        This functions takes the video link, splits it and returns the video id

    parameters: 
        video link

    returns: 
        video id
    """

    video_link_split = video_link.split("=")
    video_id = video_link_split[1]

    return video_id
