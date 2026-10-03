from chunking import split_document
from document import create_document
from llm import generate_answer
from transcript import get_transcript
from vector_store import create_vector_store, search_documents


def answer_question(
    vector_store,
    question: str,
    k: int = 3,
) -> str:
    documents = search_documents(
        vector_store=vector_store,
        query=question,
        k=k,
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return generate_answer(
        context=context,
        question=question,
    )


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    print("Fetching transcript...")

    transcript = get_transcript(video_url)

    document = create_document(
        transcript=transcript,
        video_id="dQw4w9WgXcQ",
    )

    chunks = split_document(document)

    print(f"Transcript length: {len(transcript)} characters")
    print(f"Number of chunks: {len(chunks)}")

    print("\nCreating vector store...")

    vector_store = create_vector_store(chunks)

    while True:
        question = input(
            "\nAsk a question (or type 'exit'): "
        ).strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        print("\nGenerating answer...")

        answer = answer_question(
            vector_store=vector_store,
            question=question,
        )

        print("\nAnswer:")
        print(answer)