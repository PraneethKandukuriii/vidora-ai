try:
    from .chunking import split_document
    from .document import create_document
    from .intent import detect_intent
    from .llm import generate_answer
    from .transcript import extract_video_id, get_transcript
    from .vector_store import create_vector_store, search_documents
except ImportError:  # pragma: no cover - direct script execution
    from chunking import split_document
    from document import create_document
    from intent import detect_intent
    from llm import generate_answer
    from transcript import extract_video_id, get_transcript
    from vector_store import create_vector_store, search_documents


def answer_question(
    vector_store,
    question: str,
    chat_history: list[tuple[str, str]],
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

    history = "\n".join(
        f"User: {user_question}\nAssistant: {answer}"
        for user_question, answer in chat_history
    )

    prompt = f"""
You are Vidora, an AI assistant that answers questions about a YouTube video.

Use the video context and conversation history to answer the user's question.

Conversation history:
{history}

Video context:
{context}

Current question:
{question}

Answer clearly, naturally, and with enough detail to be useful.

Follow these rules:
- Give a direct answer first.
- For simple questions, answer in 2-4 sentences.
- For explanation questions, give a clear explanation in 1-3 short paragraphs.
- For questions asking for main points, use 3-5 concise bullet points.
- Use simple language that is easy to understand.
- Do not repeat unnecessary information.
- Do not make up information that is not supported by the video context.
- Use conversation history only when necessary to understand references such as
  "it", "that", "the first one", or "what you said earlier".
- If the answer cannot be found in the video context, say:
  "I couldn't find the answer in the video."
"""

    return generate_answer(
        context=prompt,
        question=question,
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

            elif intent == "transcript":
                print(
                    "\nVidora: The transcript is available "
                    "from the video you provided."
                )

            elif intent == "summary":
                print("\nVidora: Summary feature is coming next.")

            else:
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