from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document   

def split_document(document: Document) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    return splitter.split_documents([document])


if __name__ == "__main__":
    document = Document(
    page_content=" ".join(
        f"This is sentence number {i} about machine learning and artificial intelligence."
        for i in range(100)
    ),
    metadata={
        "source": "youtube",
        "video_id": "dQw4w9WgXcQ",
    },
)

    chunks  = split_document(document)

    print(f"Number of chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:\n{chunk.page_content}\n")

    print("Metadata:", chunk.metadata)

