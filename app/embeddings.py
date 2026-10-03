import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def create_embeddings_model() -> GoogleGenerativeAIEmbeddings:
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        api_key=os.getenv("GOOGLE_API_KEY"),
    )


if __name__ == "__main__":
    embeddings_model = create_embeddings_model()

    text = "This is a sample text for generating embeddings."

    embedding_vector = embeddings_model.embed_query(text)

    print("Embedding dimensions:", len(embedding_vector))
    print("First 10 values:", embedding_vector[:10])