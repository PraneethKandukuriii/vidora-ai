try:
    from .chunking import split_document
    from .document import create_document
    from .intent import detect_intent
    from .llm import generate_response
    from .retrieval import adaptive_search
    from .transcript import extract_video_id, get_transcript
    from .vector_store import create_vector_store
except ImportError:  # pragma: no cover - direct script execution
    from chunking import split_document
    from document import create_document
    from intent import detect_intent
    from llm import generate_response
    from retrieval import adaptive_search
    from transcript import extract_video_id, get_transcript
    from vector_store import create_vector_store
    


def answer_question(
    vector_store,
    question: str,
    chat_history: list[tuple[str, str]],
) -> str:
    

    documents = adaptive_search(
    vector_store=vector_store,
    query=question,
)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    history = "\n".join(
        f"User: {user_question}\nAssistant: {answer}"
        for user_question, answer in chat_history
    )

    return generate_response(
        user_request=question,
        context=context,
        conversation_history=history,
    )


if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ").strip()

    try:
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

        print("\nVideo processed successfully.")
        print("You can now ask questions about the video.")
        print("Type 'exit' when you're finished.")

        chat_history = []

        while True:
            question = input("\nYou: ").strip()

            if question.lower() == "exit":
                print("\nGoodbye!")
                break

            if not question:
                print("Please enter a question.")
                continue

            intent = detect_intent(question)

            if intent == "casual":
                print("\nVidora: Got it.")
                continue

            if intent == "transcript":
                print(
                    "\nVidora: The transcript is available "
                    "from the video you provided."
                )
                continue

            if intent == "summary":
                print(
                    "\nVidora: Summary mode is not connected yet."
                )
                continue

            if intent == "teach":
                print(
                    "\nVidora: Teach Mode is not connected yet."
                )
                continue

            print("\nVidora: Thinking...")

            answer = answer_question(
                vector_store=vector_store,
                question=question,
                chat_history=chat_history,
            )

            print(f"\nVidora: {answer}")

            chat_history.append(
                (question, answer)
            )

    except ValueError as error:
        print(f"\nError: {error}")