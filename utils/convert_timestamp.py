def process_timestamps(timestamp):
    min = int(timestamp)
    sec = (timestamp - min) * 100

    total_seconds = (min * 60) + sec

    # Calculate hours, minutes, and seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
