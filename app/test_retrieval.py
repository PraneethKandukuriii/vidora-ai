from .chunking import split_document
from .document import create_document
from .transcript import extract_video_id, get_transcript
from .vector_store import (
    create_vector_store,
    search_documents_with_scores,
)


def main() -> None:
    video_url = input("Enter YouTube URL: ").strip()

    video_id = extract_video_id(video_url)

    print("\nFetching transcript...")

    transcript = get_transcript(video_url)

    document = create_document(
        transcript=transcript,
        video_id=video_id,
    )

    chunks = split_document(document)

    print(f"Transcript length: {len(transcript)} characters")
    print(f"Number of chunks: {len(chunks)}")

    print("\nCreating vector store...")

    vector_store = create_vector_store(chunks)

    query = input("\nEnter a question: ").strip()

    results = search_documents_with_scores(
        vector_store=vector_store,
        query=query,
        k=min(6, len(chunks)),
    )

    print("\nRetrieval results:")

    for index, (document, score) in enumerate(
        results,
        start=1,
    ):
        print(f"\n--- Result {index} ---")
        print(f"Score: {score:.4f}")
        print(f"Content: {document.page_content[:300]}")


if __name__ == "__main__":
    main()