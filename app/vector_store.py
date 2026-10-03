from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from embeddings import create_embeddings_model


def create_vector_store(documents: list[Document]) -> FAISS:
    embeddings_model = create_embeddings_model()

    return FAISS.from_documents(
        documents,
        embeddings_model,
    )


def search_documents(
    vector_store: FAISS,
    query: str,
    k: int = 3,
) -> list[Document]:
    return vector_store.similarity_search(
        query,
        k=k,
    )


if __name__ == "__main__":
    from chunking import split_document
    from document import create_document
    from transcript import get_transcript

    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    transcript = get_transcript(video_url)

    document = create_document(
        transcript=transcript,
        video_id="dQw4w9WgXcQ",
    )

    chunks = split_document(document)

    print(f"Transcript length: {len(transcript)} characters")
    print(f"Number of chunks: {len(chunks)}")

    vector_store = create_vector_store(chunks)

    query = "What is this video about?"

    results = search_documents(
        vector_store,
        query,
    )

    print(f"\nRetrieved {len(results)} relevant chunks:\n")

    for index, result in enumerate(results, start=1):
        print(f"--- Result {index} ---")
        print(result.page_content[:500])
        print("Metadata:", result.metadata)
        print()