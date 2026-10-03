from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url : str) -> str:
    video_id = video_url.split("v=")[1]

    print(f"Fetching transcript for video ID: {video_id}")

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    transcript_text = ""

    transcript_text = " ".join(snippet.text for snippet in transcript)


    return transcript_text










