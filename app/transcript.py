from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(video_url: str) -> str:
    parsed_url = urlparse(video_url.strip())

    if parsed_url.hostname in {"www.youtube.com", "youtube.com", "m.youtube.com"}:
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]

        elif parsed_url.path.startswith("/shorts/"):
            video_id = parsed_url.path.split("/shorts/")[1].split("/")[0]

        else:
            video_id = None

    elif parsed_url.hostname == "youtu.be":
        video_id = parsed_url.path.strip("/").split("/")[0]

    else:
        video_id = None

    if not video_id:
        raise ValueError("Invalid YouTube URL.")

    return video_id


def get_transcript(video_url: str) -> str:
    video_id = extract_video_id(video_url)

    print(f"Fetching transcript for video ID: {video_id}")

    api = YouTubeTranscriptApi()
    transcript = api.fetch(
    video_id,
    languages=["en-IN", "en"],
)

    return " ".join(
        snippet.text
        for snippet in transcript
    )


if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ").strip()

    try:
        transcript = get_transcript(video_url)

        print(f"\nTranscript fetched successfully.")
        print(f"Transcript length: {len(transcript)} characters")

    except ValueError as error:
        print(f"Error: {error}")









