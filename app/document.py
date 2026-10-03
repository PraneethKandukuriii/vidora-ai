from langchain_core.documents import Document


def create_document(transcript: str, video_id: str) -> Document:
    return Document(
        page_content=transcript,
        metadata={
            "source": "youtube",
            "video_id": video_id,
        },
    )

if __name__ == "__main__":
    transcript = "This is a sample YouTube transcript."

    document = create_document(
        transcript=transcript,
        video_id="dQw4w9WgXcQ",
    )

    print("Content:")
    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)