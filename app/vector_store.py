from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from embeddings import create_embeddings_model


def create_vector_store(documents: list[Document]) -> FAISS:
    embeddings_model = create_embeddings_model()

    return FAISS.from_documents(
        documents,
        embeddings_model,
    )


if __name__ == "__main__":
    documents = [
        Document(
            page_content="Machine learning allows computers to learn from data.",
            metadata={"source": "youtube", "video_id": "demo123"},
        ),
        Document(
            page_content="Neural networks are commonly used in deep learning.",
            metadata={"source": "youtube", "video_id": "demo123"},
        ),
        Document(
            page_content="Python is widely used for artificial intelligence.",
            metadata={"source": "youtube", "video_id": "demo123"},
        ),
    ]

    vector_store = create_vector_store(documents)

    print("FAISS vector store created successfully.")