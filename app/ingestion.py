try:
    from .chunking import split_document
    from .document import create_document
    from .transcript import extract_video_id, get_transcript
    from .vector_store import create_vector_store
    from .embeddings import create_embeddings_model
except ImportError:  # pragma: no cover - direct script execution
    from chunking import split_document
    from document import create_document
    from transcript import extract_video_id, get_transcript
    from vector_store import create_vector_store
    from embeddings import create_embeddings_model


def process_video(video_url: str):
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

    return {
        "video_id": video_id,
        "transcript": transcript,
        "chunks": chunks,
        "vector_store": vector_store,
    }